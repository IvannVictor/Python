from time import sleep

print('\033[36m=-'*30)
print('\033[1:33mVamos calcular se voce consegue finaciar sua futura casa?')
print('\033[36m=-\033[m'*30)

sleep(1)
casa = str(input('Qual o valor da casa? R$')).strip().replace(',', '.')
salario = str(input('Qual o seu salario? R$')).strip().replace(',', '.')
anos = int(input('Quantos anos pretende passar pagando? '))

casa = float(casa)
salario = float(salario)

ms = anos * 12
vm = casa / ms
sm = salario - (salario * 30/100)
salario = salario - sm

sleep(3)
print('\033[1:35mHummmmmm, calma estamos calculando\033[m')

sleep(2)
print('\033[1:34mPronto, esta ai o resultado\033[m')

sleep(1)
if vm > salario:
    print('O valor mensal que vai fica essa casa é de \033[31mR${:.2f}\033[m, 30% do seu salario é \033[33mR${:.2f}\033[m,'
          ' com esse valor voce não vai conseguir financiar essa casa'.format(vm, salario))
else:
    print('O valor mensal dessa casa fica \033[31mR${:.2f}\033[m, e 30% do seu salario é \033[33m{:.2f}\033[m e '
          'com isso voce consegue finaciar sua casa nova \033[36mParabens\033[m'.format(vm, salario))
