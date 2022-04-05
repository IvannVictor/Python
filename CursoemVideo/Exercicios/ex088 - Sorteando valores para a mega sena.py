from random import randint
from time import sleep

tot = 1
lista = list()
jogos = list()

print('-=' * 30)
print(f'{"Sorteador da mega sena":^60}')
print('-=' * 30)

quant = int(input('Quantos jogos voce quer que eu sortei para voce? '))

while tot <= quant:  # Enquanto não for igual a quantidade escolhida
    cont = 0
    while True:
        num = randint(0, 60)

        if num not in lista:
            lista.append(num)
            cont = cont + 1

        if cont == 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot = tot + 1


print()
print('--' * 30)
print(f'{"Jogos sorteados":^60}')
print('--' * 30)
sleep(1)

for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {l}')
print('--' * 11, 'Boa Sorte', '---' * 9)
