import calc_imc


print('Gerando e validando os dados para calculo de imc...')

verif = 's'
valid = False

while verif == 's':

    while valid == False:
        sexo = input('Entre com o sexo(M/F): ').lower()
        if sexo == 'm' or sexo == 'f':
            valid = True
        else:
            print('Sexo inválido!')

    valid = False

    while valid == False:
        peso = input('Entre com o peso: ')
        try:
            peso = float(peso)
            if peso > 0 and peso < 400:
                valid = True
            else:
                print('Entre com o peso de um humano!')
        except:
            print('Valor do peso inválido!')

    valid = False

    while valid == False:
        altura = input('Entre com a altura: ')
        try:
            altura = float(altura)
            if altura > 0 and altura < 3:
                valid = True
            else:
                print('Entre com a altura de um humano!')
        except:
            print('Valor da altura inválido!')

    valid = False

    print('\n Sexo:', sexo, 'Peso:', peso, 'Altura:', altura)

    print(calc_imc.classe_imc(sexo,peso,altura))

    verif = input("Deseja verificar mais imc's(S/N)?")
