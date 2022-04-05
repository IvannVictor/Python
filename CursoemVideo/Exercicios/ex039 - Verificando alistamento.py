from datetime import date
from time import sleep

print('\033[32m=-\033[m' * 45)
print('\033[31mVamos calcular se voce ainda tem que se alistar no exercito ou se já passou da hora\033[m')
print('\033[32m=-\033[m' * 45)

sleep(1)

ano = int(input('Digite o seu ano de nascimeto '))

idade = date.today().year - ano

sleep(2)
print('\033[33mInteressante.....\033[m')

sleep(2)
if idade < 18:
    print('\033[34mVoce ainda não tem idade para o alistamento militar\033[m')
    re = 18 - idade
    print('Faltam \033[36m{}\033[m anos para seu alistamento'.format(re))
    al = date.today().year + re
    print('Seu alistamento será em \033[36m{]\033[m'.format(al))

elif idade == 18:
    print('Voce já tem \033[36m18 anos\033[m, idade para o alistamento, acesse a pagina do governo federal e '
          'verifique uma data para apresentar-se')

else:
    ps = idade - 18
    print('Já passou \033[36m{}\033[m anos do seu alistamento'.format(ps))
    ja = date.today().year - ps
    print('O seu alistamento foi em \033[36m{}\033[m'.format(ja))