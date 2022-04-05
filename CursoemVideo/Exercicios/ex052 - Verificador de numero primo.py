n = int(input('Digite um numero: '))
div = 0

for c in range(1, n+1, 1):
    if n % c == 0:
        print('\033[34m', end='')
        div = div + 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')

print('\n\033[mO numero \033[33m{}\033[m foi divisivel \033[32m{}\033[m vezes'.format(n, div))

if div == 2:
    print('Por isso ele é \033[35msim\033[m um \033[35mnumero primo\033[m')
else:
    print('Por isso ele \033[31mnão\033[m é um \033[31mnumero primo\033[m')
