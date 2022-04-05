pessoa = list()
temp = list()
mai = men = 0

while True:
    temp.append(str(input('Digite o nome da pessoa: ')).title().strip())
    temp.append(float(input('Digite o peso da pessoa: ')))

    if len(pessoa) == 0:  # Validar antes de preencher os dados na lista principal
        mai = men = temp[1]

    if temp[1] > mai:
        mai = temp[1]

    if temp[1] < men:
        men = temp[1]

    pessoa.append(temp[:])
    temp.clear()

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja cadastrar mais pessoas? (S/N)')).strip().upper()[0]
    if op == 'N':
        break

print(f'Nessa base de dados foram cadastradas, {len(pessoa)} pessoas')
print(f'Maior peso foi {mai}Kg, peso de', end=' ')
for i, p in enumerate(pessoa):  # Não precisa colocar o enumerate
    if mai == p[1]:
        print(f' {p[0]}', end=' ')

print()  # Print para pular linha
print(f'Menor peso foi de {men}Kg, peso de', end=' ')
for i, p in enumerate(pessoa):
    if men == p[1]:
        print(f' {p[0]}', end=' ')
