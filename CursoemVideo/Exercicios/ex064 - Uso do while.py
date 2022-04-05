v = 0
c = 0
s = 0
v = int(input('Digite o valor  '))

while v != 999:
    c = c + 1
    s = s + v
    v = int(input('Digite o valor  '))
print('Digitou {} valores, total de {}'.format(c, s))
