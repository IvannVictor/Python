valores = []

while True:
    valores.append(int(input('Digite um valor para ser adicinado a lista: ')))

    op = ' '
    while op not in 'SN':
        op = str(input('Gostaria de colocar mais numeros? [S/N]')).upper().strip()[0]

    if op == 'N':
        break

print('\n-=' * 30)
print(f'Foram digitados {len(valores)} valores')
print(f'Os valores adicinados foram {valores}')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente é: {valores}')

if 5 in valores:
    print('O numero 5 esta incluso na lista')
else:
    print('O numero 5 não esta incluso nessa lista')
print('-=' * 30)
