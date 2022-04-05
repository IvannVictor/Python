n1 = int(input('Digite um numero: '))

if n1 == '0' or '2' or '4' or '6' or '8':
    print('O numero que voce digitou {}, é um numero PAR'.format(n1))
else:
    print('O numero que voce digitou {}, é IMPAR'.format(n1))

print('Correção do exercicio ')

r = n1 % 2

if r == 0:
    print('O numero {} é PAR'.format(n1))
else:
    print('O numero {} é IMPAR'.format(n1))
