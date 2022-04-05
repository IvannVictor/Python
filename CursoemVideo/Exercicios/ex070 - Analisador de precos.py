soma = totm = co = 0
mpre = ''
prod = ' '
while True:
    produto = str(input('Qual o produto? ')).strip().title()
    valor = float(input('Digite o valor R$'))

    co = co + 1
    soma = soma + valor

    if valor > 1000:
        totm = totm + 1

    if co == 1:
        mpre = valor
        prod = produto
    else:
        if mpre > valor:
            mpre = valor
            prod = produto

    op = ' '
    while op not in 'SP':
        op = str(input('Tem mais produtos? ')).strip().upper()[0]

    if op == 'P':
        break

print(f'\nTotal de R${soma:.2f}')
print(f'O mais barato é o {prod} que tem o valor de R${mpre:.2f}')
if totm == 0:
    print('Nenhum produto custa mais de mil reais')
elif totm == 1:
    print('Apenas um pruduto custa mais de mil reais')
else:
    print(f'{totm} custao mais de mil reias')
