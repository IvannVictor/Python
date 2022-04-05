import random
from time import sleep

jogada = 0
compu = 0
jogador = 1


print('''\n\033[34mVamos brincar!!!\033[m
\033[35mTente adivinhar o numero que o computador pensou!!\033[m''')
sleep(1)

while jogador != compu:

    jogador = int(input('\nDigite um valor: '))
    compu = random.randint(1, 10)
    jogada = jogada + 1

    if jogador == compu:
        print('''\033[32mVoce venceu 
\033[mComputador colocou \033[36m{}\033[m e voce \033[37m{}\033[m
E para isso voce jogou \033[33m{}\033[m vezes'''.format(compu, jogador, jogada))

    else:
        print('''\033[31mVoce errou, tente novamente\033[m
Computador colocou \033[36m{}\033[m e voce \033[37m{}\033[m'''.format(compu, jogador))
