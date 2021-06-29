import random


def megasena():

    n_jogos = 0

    valid = False

    while valid == False:
        nj = input('Digite a quantidade de jogos da MegaSena que deseja gerar? ')
        try:
            nj = int(nj)

            if nj > 0:
                valid = True

                while n_jogos < nj:

                    jogo = []

                    while len(jogo) < 6:
                        num = random.randint(1,60)
                        if num in jogo:
                            continue
                        else:
                            jogo.append(num)

                    print('\n', sorted(jogo))

                    n_jogos += 1

                print('\n Boa sorte!')
            else:
                print('[ERRO] Entre com um número maior que 0!')

        except:
            print('[ERRO] Entre com um número válido! Somente números!')

megasena()
