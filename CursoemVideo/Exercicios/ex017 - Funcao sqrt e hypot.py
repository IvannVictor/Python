from math import sqrt,hypot
n1 = float(input('Vamos calcular a Hipotenusa\nDigite o valor do Cateto Adjacente '))
n2 =float(input('Digite o valor do Cateto Oposto '))
hi = hypot(n1, n2)

print('O valor da Hipotenusa é {:.2f}'.format(sqrt((n1**2) + (n2**2))))
print('O VALOR DA HIPOTENUSA USANDO A CLASSE MATH {:.2f}'.format(hi))
