from datetime import date
from time import sleep

print('\033[36m=-\033[m' * 30)
print('\033[34mVamos ver qual classe voce vai fazer parte na natação\033[m')
print('\033[36m=-\033[m' * 30)

sleep(2)
ns = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ns

sleep(2)
print('\033[33mCalma, to vendo aqui.....\033[m')

sleep(3)
if idade <= 9:
    print('Voce faz parte da classe \033[32mMIRIM\033[M')
elif idade <= 14:
    print('Voce faz parte da classe \033[36mINFANTIL\033[m')
elif idade <= 19:
    print('Voce faz parte da classe \033[34mJUNIOR\033[m')
elif idade == 20:
    print('Voce faz parte da classe \033[35mSENIOR\033[m')
else:
    print('Voce faz parte da classe \033[35mMASTER\033[m')
