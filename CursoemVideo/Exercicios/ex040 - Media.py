from time import sleep

print('\033[31m=-\033[m' * 25)
print('\033[32mSera que voce passou de ano?\033[m')
print('\033[31m=-\033[m' * 25)

sleep(2)
n1 = str(input('Digite a sua nota no primeiro semestre: ')).strip().replace(',', '.')
n2 = str(input('Digite a sua nota do segundo semestre: ')).strip().replace(',', '.')
n1 = float(n1)
n2 = float(n2)
media = (n1 + n2) / 2

sleep(2)
print('\033[36mEstamos calculando\033[m')

sleep(3)
if media < 5:
    print('Sua media foi \033[33m{:.1f}\033[m, com isso voce foi \033[33mreprovado\033[m, por favor estude mais!!!'.format(media))
elif media < 6.9:
    print('Sua media foi \033[33m{:.1f}\033[m, com isso voce ficou de \033[33mrecuperação\033[m, vamos estudar!!'.format(media))
else:
    print('Sua media foi \033[35m{:.1f}\033[m, com isso voce foi \033[35maprovado\033[m!! Parabens!!'.format(media))
