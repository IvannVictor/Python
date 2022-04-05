from random import choice

n1 = str(input('Vamos sortear um aluno\nDigite um nome '))
n2 = str(input('Digite outro '))
n3 = str(input('Digite mais outro '))
n4 = str(input('Digite o ultimo nome '))

lista = [n1, n2, n3, n4]
res = choice(lista)

print('O nome escolhido foi {}'.format(res))
