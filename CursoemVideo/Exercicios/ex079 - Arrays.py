valores = list()
pri = 0
seg = 0
while True:
    n = int(input('Digite um valor para ser adicinado a lista: '))

    if n not in valores:
        print(f'Valor {n} adicinado com sucesso')
        valores.append(n)
    else:
        print(f'O valor {n} já foi adicinado anteriormente')

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja cadastrar mais valores? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break

valores.sort()
print(f'Os valores adicinados a lista foram {valores}')
