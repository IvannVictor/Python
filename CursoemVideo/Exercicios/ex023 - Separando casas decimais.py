frase = str(input('Vamos separar um numero pelas respectivas casas\nDigite um numero entre 0 e 9999: '))

print('''Casa da Unidade: {}
Casa da Dezena: {}
Casa da Centena: {}
Casa do Milhar: {}'''.format(frase[-1:], frase[2:3], frase[1:2], frase[0:1]))

print('Correção')
nun = int(input('Vamos separar um numero pelas respectivas casas\nDigite um numero entre 0 e 9999: '))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10
print('''Casa da Unidade: {}
Casa da Dezena: {}
Casa da Centena: {}
Casa do Milhar: {}'''.format(u, d, c, m))
