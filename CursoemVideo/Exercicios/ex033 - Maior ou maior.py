n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))
n3 = int(input('Digite mais um por favor: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 < n1 and n3 < n2:
    maior = n3

print('Maior valor foi {}'.format(maior))
print('Menor valor foi {}'.format(menor))
