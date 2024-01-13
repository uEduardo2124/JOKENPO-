from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

while True:
    try:
        player = str(
            input('Digite sua jogada(somente pedra, papel ou tesoura serão aceitos :D): ')).strip().capitalize()
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
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {player}')
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
