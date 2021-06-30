import requests
import json
from datetime import date
import urllib.parse


accuweatherAPIKey = 'ACC-WEATHER-API-KEY'
mapboxToken = 'MAP-BOX-TOKEN'
week_days = ['Domingo', 'Segunda-feira', 'Terça-feira','Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

def getCoord():
    r = requests.get('http://www.geoplugin.net/json.gp')

    if (r.status_code != 200):
        print('Não foi possível obter a coordenada.')
        return None
    else:
        try:
            localização = json.loads(r.text)
            coordenadas = {}
            coordenadas['lat'] = localização['geoplugin_latitude']
            coordenadas['long'] = localização['geoplugin_longitude']
            return coordenadas
        except:
            return None

def getLocalCode(lat,long):
    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?" \
    + "apikey=" + accuweatherAPIKey +"&q=%20" + lat + "%2C" + long + "&language=pt-br"

    r = requests.get(locationAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o codigo.')
        return None
    else:
        try:
            locationResponse = json.loads(r.text)
            localInfo = {}
            localInfo['nomeLocal'] = locationResponse['LocalizedName'] + ", " \
                        + locationResponse['AdministrativeArea']['LocalizedName'] + ". " \
                        + locationResponse['Country']['LocalizedName']
            localInfo['codigoLocal'] = locationResponse['Key']
            return localInfo
        except:
            return None

def getCurrentWeather(codigoLocal, nomeLocal):
    currentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
    + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

    r = requests.get(currentConditionsAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima local.')
        return None
    else:
        try:
            currentConditionsReponse = json.loads(r.text)
            climaInfo = {}
            climaInfo['textoClima'] = currentConditionsReponse[0]['WeatherText']
            climaInfo['temperatura'] = currentConditionsReponse[0]['Temperature']['Metric']['Value']
            climaInfo['nomeLocal'] = nomeLocal
            return climaInfo
        except:
            return None


def get5DailyForecasts(codigoLocal):
    dailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
    + codigoLocal + "?apikey=" + accuweatherAPIKey + "&language=pt-br"

    r = requests.get(dailyAPIUrl)
    if (r.status_code != 200):
        print('Não foi possível obter o clima local.')
        return None
    else:
        try:
            dailyReponse = json.loads(r.text)
            infoWeather = []
            for day in dailyReponse['DailyForecasts']:
                dayWeather = {}
                dayWeather['max'] = day['Temperature']['Maximum']['Value']
                dayWeather['min'] = day['Temperature']['Minimum']['Value']
                dayWeather['clima'] = day['Day']['IconPhrase']
                weekDay = int(date.fromtimestamp(day['EpochDate']).strftime("%w"))
                dayWeather['dia'] = week_days[weekDay]
                infoWeather.append(dayWeather)
            return infoWeather
        except:
            return None

def showPrev(lat, long):
    try:
        local = getLocalCode(lat,long)
        climaAtual = getCurrentWeather(local['codigoLocal'], local['nomeLocal'])
        print('Clima atual em: ' + climaAtual['nomeLocal'])
        print(climaAtual['textoClima'])
        print('Temperatura: ' + str(climaAtual['temperatura']) + '\xb0' + 'C')
    except:
        print('[ERRO] Não foi possível obter o clima atual.')

    option = input('\n Deseja ver a previsão dos próximos dias(S/N)?').lower()

    if option == 's':
        print('\n Previsão do tempo de hoje e do próximo dias.')

        try:
            dailyForecasts = get5DailyForecasts(local['codigoLocal'])
            for day in dailyForecasts:
                print('\n',day['dia'])
                print('Mínima: ' + str(round(((day['min']-32)/1.800),1)) + "\xb0" + 'C')
                print('Máxima: ' + str(round(((day['max']-32)/1.800),1)) + "\xb0" + 'C')
                print('Clima: ' + day['clima'])
                print('________________________')
        except:
            print('[ERRO] Não foi possível obter a previsão dos próximos dias.')


def localSearch(local):
    _local = urllib.parse.quote(local)
    mapboxGeocodeUrl = "https://api.mapbox.com/geocoding/v5/mapbox.places/" \
    + _local + ".json?access_token=" + mapboxToken

    r = requests.get(mapboxGeocodeUrl)
    if (r.status_code != 200):
        print('Não foi possível pesquisar o local.')
        return None
    else:
        try:
            mapboxResponse = json.loads(r.text)
            coordenadas = {}
            coordenadas['long'] = str( mapboxResponse['features'][0]['geometry']['coordinates'][0] )
            coordenadas['lat'] = str( mapboxResponse['features'][0]['geometry']['coordinates'][1] )
            return coordenadas
        except:
            return None

try:
    coordenadas = getCoord()
    showPrev(coordenadas['lat'], coordenadas['long'])

    keep = 's'

    while keep == 's':
        keep = input('\n Deseja buscar a previsão de outro local(S/N)?').lower()
        if keep != 's':
            break
        local = input("Entre com a cidade e o estado(Ex: cidade, estado ):")
        try:
            coordenadas = localSearch(local)
            showPrev(coordenadas['lat'], coordenadas['long'])
        except:
            print('[ERRO] Não foi possível buscar a previsão do local.')
except:
    print('[ERRO] Contate o suporte!')
