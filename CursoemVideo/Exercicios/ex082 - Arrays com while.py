valores = list()

while True:
    valores.append(int(input('Digite o valor que voce gostaria de armazenar nas listas: ')))

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar colocando mais numeros? ')).upper().strip()[0]
    if op == 'N':
        break

listapar = []
for i, v in enumerate(valores):
    if v % 2 == 0:
        listapar.append(v)
listapar.sort()

listaimpar = []
for i, v in enumerate(valores):
    if v % 2 == 1:
        listaimpar.append(v)
listaimpar.sort()

print('=-' * 30)
print(f'Os valores que foram adicionados a lista foram {valores}')
print(f'Dessa lista os valores pares são {listapar}')
print(f'Dessa lista os valores impares são {listaimpar}')
print('=-' * 30)
