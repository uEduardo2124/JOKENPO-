from random import randint
from time import sleep


while True:
    itens = ['Pedra', 'Papel', 'Tesoura']
    computador = randint(0, 2)

    while True:
        try:
            print('-=-' * 24)
            player = str(input('Digite sua jogada(somente pedra, papel ou tesoura serão aceitos :D): ')).strip().capitalize()
            if player in itens:
                break
            else:
                print('\033[31mEntrada inválida, por favor, digite novamente!\033[m')
        except:
            print('\033[35mERRO! Algo deu errado, por favor, tente novamente\033[m')

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')

    print('-=-' * 12)
    print(f'Computador jogou: \033[31m{itens[computador]}\033[m')
    print(f'Jogador jogou: \033[32m{player}\033[m')
    print('-=-' * 12)

    if computador == 0:
        if player == itens[0]:
            print('\033[33mEmpate\033[m!')
        elif player == itens[1]:
            print('\033[32mJOGADOR VENCEU\033[m!')
        elif player == itens[2]:
            print('\033[31mCOMPUTADOR VENCEU\033[m!')
        else:
            print('\033[7:mJOGADA INVÁLIDA\033[m')

    elif computador == 1:
        if player == itens[0]:
            print('\033[31mCOMPUTADOR VENCEU\033[m!')
        elif player == itens[1]:
            print('\033[33mEMPATE\033[m!')
        elif player == itens[2]:
            print('\033[32mJOGADOR VENCEU\033[m!')
        else:
            print('\033[7:mJOGADA INVÁLIDA\033[m')

    else:
        if player == itens[0]:
            print('\033[32mJOGADOR VENCEU\033[m!')
        elif player == itens[1]:
            print('\033[31mCOMPUTADOR VENCEU\033[m!')
        elif player == itens[2]:
            print('\033[33mEMPATE\033[m!')
        else:
            print('\033[7:mJOGADA INVÁLIDA\033[m')

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar jogando ? (Responda com sim(S) ou não (N)): ')).strip().upper()[0]
    if continuar == 'N':
        print('\033[32mObrigado por jogar! Volte sempre.\033[m')
        break
