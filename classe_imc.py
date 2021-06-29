import calc_imc


def classe_imc(sexo,peso,altura):

    print('Classificando o imc...')

    IMC = calc_imc.calc_imc(peso,altura)

    if sexo == 'm':
        if IMC < 20.7:
            return 'Abaixo do peso!', 'IMC:', IMC
        elif IMC >= 20.7 and IMC <= 26.4:
            return 'No peso normal!', 'IMC:', IMC
        elif IMC > 26.4 and IMC <= 27.8:
            return 'Marginalmente acima do peso!', 'IMC:', IMC
        elif IMC > 27.8 and IMC <= 31.1:
            return 'Acima do peso ideal!', 'IMC:', IMC
        elif IMC > 31.1:
            return 'Obeso!', 'IMC:', IMC
        else:
            return '[ERROR]Erro na classificação do imc!'

    else:
        if IMC < 19.1:
            return '\n Abaixo do peso!', 'IMC:', IMC
        elif IMC >= 19.1 and IMC <= 25.8:
            return 'No peso normal!', 'IMC:', IMC
        elif IMC > 25.8 and IMC <= 27.3:
            return 'Marginalmente acima do peso!', 'IMC:', IMC
        elif IMC > 27.3 and IMC <= 32.3:
            return 'Acima do peso ideal!', 'IMC:', IMC
        elif IMC > 32.3:
            return 'Obeso!', 'IMC:', IMC
        else:
            return '[ERROR]Erro na classificação do imc!'
