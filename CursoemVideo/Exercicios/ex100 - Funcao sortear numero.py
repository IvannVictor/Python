from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteand 5 valores para a lista')
    for c in range(0, 5):  # Sorteia os valores
        n = randint(1, 10)
        lista.append(n)  # Adiciona os valores em lista que coloca em numeros
        print(f'{n}', end=' ')
        sleep(0.2)
    print('Pronto')


def SomaPar(lista):
    soma = 0
    print('=' * 40)
    print('Os valores pares sorteados foram')
    for c in lista:
        print(f'{c}', end=' ')
        sleep(0.2)
        if c % 2 == 0:
            soma = soma + c
    print(f' e a soma deles é o total de {soma}')


numeros = list()
sorteia(numeros)
SomaPar(numeros)
