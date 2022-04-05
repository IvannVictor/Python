from random import shuffle
n1 = input('Vamos sortear a ordem de apresentação\nDigite um nome ')
n2 = input('Digite outro nome ')
n3 = input('Digite mais um ')
n4 = input('Digite o ultimo ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem ficou a seguinte {}'.format(lista))
