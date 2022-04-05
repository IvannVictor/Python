n1 = str(input('Digite o seu salario: R$')).replace(',', '.').strip()
n1 = float(n1)
if n1 > 1250:
    re = n1 + (n1*10/100)
    print('O seu salario atual é de R${:.2f} e com o aumento de 10% vai para R${:.2f}'.format(n1, re))
else:
    r = n1 + (n1*15/100)
    print('O seu salario atual é de R${:.2f} e com o aumento de 15% vai para R${:.2f}'.format(n1, r))
