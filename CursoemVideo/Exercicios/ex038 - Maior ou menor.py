from time import sleep

print('\033[34m=-\033[m' * 30)
print('\033[35mVamos  comparar valores\033[m')
print('\033[34m=-\033[m' * 30)

sleep(1)
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro  numero: '))

sleep(2)
print('\033[33mProcessanado as informação\033[m')
sleep(2)

if n1 > n2:
    print('O primeiro numero \033[31m{}\033[m é maior que o segundo numero \033[32m{}\033[m'.format(n1, n2))
elif n2 > n1:
    print('O segundo numero \033[31m{}\033[m é maior que o primeiro numero \033[32m{}\033[m'.format(n2, n1))
else:
    print('Ambos os numeros são \033[35miguais\033[m')
