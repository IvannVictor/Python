total = 0

produtos = ('Lápis', 1.75, 'Borracha', 3.50, 'Caneta', 2, 'Corretivo', 4.80, 'Caderno 10 materias', 25.80)


print('\n')
print('-' * 39)
print(f'{"Nota fiscal":^39}')
print('-' * 39)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
        total = total + produtos[pos]
print('-' * 39)
print(f'{"total à pagar":.<30}R${total:>7.2f}')
print('-' * 39)
