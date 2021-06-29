'''
##Lista de exercicios em python

peso1 = int(input("Entre com o peso da primeira prova:"))
peso2 = int(input("Entre com o peso da segunda prova:"))

nota1 = float(input("Entre com a primeira nota do aluno:"))
nota2 = float(input("Entre com a segunda nota do aluno:"))

media = ((peso1*nota1)+(peso2*nota2))/(peso1+peso2)

print('A media poderada é:', media)

######################################################

idade = int(input('Digite a sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()
cidade = input('Digite a cidade: ').lower()

if cidade == 'rio' or cidade == 'sao paulo' or cidade == 'minas':

    if sexo == 'm':
        if idade < 18:
            print('Homem menor de idade!', sexo, idade, 'anos', cidade)
        else:
            print('Homem maior de idade!', sexo, idade, 'anos', cidade)

    elif sexo == 'f':
        if idade < 18:
            print('Mulher menor de idade!', sexo, idade, 'anos', cidade)
        else:
            print('Mulher maior de idade!', sexo, idade, 'anos', cidade)
    else:
        print('[ERROR]Erro na entrada de dados.')
else:
    print('[ERROR]Teste da regiao sudeste')

######################################################

cont = 0

while cont < 4:

    nome = input('Digite o nome:')
    np1 = float(input('Nota da prova 1:'))
    np2 = float(input('Nota da prova 2:'))
    faltasT = float(input('Total de faltas:'))

    media = (np1+np2)/2
    assiduidade = 100-((faltasT*100)/20)

    if media < 6 and assiduidade < 70:
        print('Nome do aluno:', nome, '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
        print('\n Reprovado por faltas e por média!')
    elif media < 6 and assiduidade >= 70:
        print('Nome do aluno:', nome, '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
        print('\n Reprovado por média!')
    elif media >= 6 and assiduidade < 70:
        print('\n Nome do aluno:', nome, '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
        print('\n Reprovado por faltas!')
    else:
        print('Nome do aluno:', nome, '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
        print('\n Aprovado!')

    cont += 1

######################################################

lista = ['dado1','dado2','dado3']
nome = 'Lucas'

for i in nome:
    print(i)

######################################################

lista = [1000,450,300,920,600]

tot = 0

for i in lista:
    tot += i
    print(tot)

######################################################

dict = {'chave1':'valor1','chave2':'valor2','chave3':'valor3'}

for i in dict:
    print(i,dict[i])

######################################################

list = [['el1','el2'],['it1','it2'],['obj1','obj2']]

for i in list:
    print(i)
    for j in i:
        print(j)

######################################################

for i in range(0,10):
    print(i)
    print('\n', 10-i)

######################################################

produtos = []
fatura = 0.0

while True:
    prod = input('Entre com o nome do produto:')
    preco = float(input('Entre com o preço do produto:'))
    produtos += ['Produto:', prod, 'Preço:', preco]

    fatura += preco

    resp = input('Deseja comprar mais algum produto(s/n)? ').lower()

    if resp == 'n':
        break
    elif resp == 's':
        continue
    else:
        print('Erro!')
        break

print('\n',produtos)
print('O total da fatura é: R$',fatura)
'''
######################################################

def fatura_produto():

    print('Função de calculo de fatura de compra de produtos! \n ')

    repetir = 's'
    fatura = []
    total = 0
    valid_preco = False

    while repetir == 's':
        produto = input('Digite o nome do produto:')

        while valid_preco == False:
            preco = input('Digite o preço do produto:')
            try:
                preco = float(preco)
                if preco > 0:
                    valid_preco = True
                else:
                    print('Preço inválido!')
            except:
                print("Formato de preço inválido! Use apenas números e separe os centavos por '.' .")

        fatura.append([produto,preco])
        total += preco
        valid_preco = False
        repetir = input('Deseja comprar mais algum produto(S/N)?').lower()

    for i in fatura:
        print(i[0],'-',i[1])

    print('O total da fatura é: R$',total)

######################################################

def cadastra_nota_aluno():

    print('Função de cadastro de nota e presença de aluno com status de aprovação. \n ')

    lp = 's'
    valid_nota = False

    while lp == 's':

        nome = input('Digite o nome:')

        while valid_nota == False:
            np1 = input('Nota da prova 1:')
            try:
                np1 = float(np1)
                if np1 >= 0 and np1 <= 10:
                    valid_nota = True
                else:
                    print('Nota inválida!A nota deve ser entre 0 e 10')
            except:
                print("Formato de nota inválido!")

        valid_nota = False

        while valid_nota == False:
            np2 = input('Nota da prova 2:')
            try:
                np2 = float(np2)
                if np2 >= 0 and np2 <= 10:
                    valid_nota = True
                else:
                    print('Nota inválida!A nota deve ser entre 0 e 10!')
            except:
                print("Formato de nota inválido!")

        valid_nota = False

        while valid_nota == False:
            faltasT = input('Número de faltas:')
            try:
                faltasT = float(faltasT)
                if faltasT >= 0 and faltasT <= 20:
                    valid_nota = True
                else:
                    print('Falta inválida!As faltas devem ser entre 0 e 20!')
            except:
                print("Formato de faltas inválido!")

        valid_nota = False

        media = (np1+np2)/2

        assiduidade = 100-((faltasT*100)/20)

        if media < 6 and assiduidade < 70:
            print('\n Nome do aluno:', nome.title(), '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
            print('\n Reprovado por faltas e por média!')
        elif media < 6 and assiduidade >= 70:
            print('\n Nome do aluno:', nome.title(), '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
            print('\n Reprovado por média!')
        elif media >= 6 and assiduidade < 70:
            print('\n Nome do aluno:', nome.title(), '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
            print('\n Reprovado por faltas!')
        else:
            print('\n Nome do aluno:', nome.title(), '\n Média:', media, '\n Assiduidade:', assiduidade, '%')
            print('\n Aprovado!')

        lp = input('\n Deseja continuar registrando alunos(S/N)?').lower()

######################################################

def imc(peso, altura):
    print('Calculando o imc...')
    valor_imc = peso/(altura*altura)
    return(valor_imc)

######################################################

def calc_imc():
    print('Classificando o imc por sexo...')

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
                valid = True
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

        IMC = imc(peso,altura)

        print('\n Sexo:', sexo, 'Peso:', peso, 'Altura:', altura, 'IMC:', IMC)

        if sexo == 'm':
            if IMC < 20.7:
                print('\n Abaixo do peso!')
            elif IMC >= 20.7 and IMC <= 26.4:
                print('\n No peso normal!')
            elif IMC > 26.4 and IMC <= 27.8:
                print('\n Marginalmente acima do peso!')
            elif IMC > 27.8 and IMC <= 31.1:
                print('\n Acima do peso ideal!')
            elif IMC > 31.1:
                print('\n Obeso!')

        else:
            if IMC < 19.1:
                print('\n Abaixo do peso!')
            elif IMC >= 19.1 and IMC <= 25.8:
                print('\n No peso normal!')
            elif IMC > 25.8 and IMC <= 27.3:
                print('\n Marginalmente acima do peso!')
            elif IMC > 27.3 and IMC <= 32.3:
                print('\n Acima do peso ideal!')
            elif IMC > 32.3:
                print('\n Obeso!')

        verif = input("Deseja verificar mais imc's(S/N)?")

######################################################

def class_imc(sexo,peso,altura):

    print('Classificando o imc...')

    IMC = imc(peso,altura)

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

######################################################

def valida():
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

        print(class_imc(sexo,peso,altura))

        verif = input("Deseja verificar mais imc's(S/N)?")

######################################################

import random


def megasena():
    jogo = []

    while len(jogo) < 6:
        num = random.randint(1,60)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    print(sorted(jogo))

######################################################
# Site para instalar o built package: matplotlib.org
# Outros sites de built packages:
# - Jogos - pygame.org
# - GUI Toolkit(interface) - wxpython.org
# - BD(sql) - sqlalchemy.org
# - Beautiful Soup - crummy.com
# - Math, science and engineering - scipy.org
######################################################


import matplotlib.pyplot as plt


def matplot_aula():
    x = [1,2,3,4,5,6]
    y = [1500,1800,1300,1900,2100,2000]

    legenda = ['Jan','Fev','Mar','Abr','Mai','Jun']
    plt.xticks(x,legenda)

    plt.plot(x,y)

    plt.show()

######################################################

import time as t
import matplotlib.pyplot as plt

def time_matplot_aula():
    tempos = []
    vezes = []
    legenda = []
    vez = 1

    wd = input('Entre com a palavra que deseja marcar o tempo de digitação: ').lower()
    n = int(input('Contador de tempo de digitação da palavra acima, que será digitada quantas vezes? '))

    while vez <= n:
        inicio = t.perf_counter()
        input('Digite a palavra: ')
        fim = t.perf_counter()
        tempo = round(fim-inicio,2)
        tempos.append(tempo)
        vezes.append(vez)
        vez += 1
        legenda += [vez-1]
    plt.xticks(vezes,legenda)

    plt.plot(vezes,tempos)
    plt.show()
