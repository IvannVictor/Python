from random import randint
from time import sleep

print('\033[33m=-\033[m' * 30)
print('\033[36mVamos brincar de JOKENPO\033[m')
print('\033[33m=-\033[m' * 30)

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''\033[31mSuas opçoes
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura\033[m''')
jo = int(input('Qual sera a sua escolha? '))

print('\033[37mJO\033[m')
sleep(1)
print('\033[34mKENN\033[m')
sleep(1)
print('\033[36mPOO!!\033[m')

print('\033[33m=-\033[m' * 30)
print('Voce esoclheu \033[32m{}\033[m'.format(itens[jo]))
print('Computador escolheu \033[32m{}\033[m'.format(itens[pc]))
print('\033[33m=-\033[m' * 30)

if pc == 0:
    if jo == 0:
        print('EMPATE')

    elif jo == 1:
        print('VOCE VENCEU!!')

    elif jo == 2:
        print('COMPUTADOR VENCEU!!')

    else:
        print('JOGADA INVALIDA')

elif pc == 1:
    if jo == 0:

        print('COMPUTADOR VENCEU!!')
    elif jo == 1:
        print('EMPATE')

    elif jo == 2:
        print('VOCE VENCEU!!')

    else:
        print('JOGADA INVALIDA')

elif pc == 2:
    if jo == 0:
        print('VOCE VENCEU!!')

    elif jo == 1:
        print('COMPUTADOR VENCEU!!')

    elif jo == 2:
        print('EMPATE')

    else:
        print('JOGADA INVALIDA')
