print('=-' * 30)
print('Cadastro de pessoas')
print('=-' * 30)

midade = 0
mu = 0
ho = 0

while True:
    idade = int(input('Digite a idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da pessoa: ')).upper().strip()[0]

    if sexo == 'F':
        if idade < 18:
            mu = mu + 1

    if idade > 18:
        midade = midade + 1

    if sexo == 'M':
        ho = ho + 1

    op = ' '
    while op not in 'SP':
        op = str(input('Vai cadastrar mais pessoas? ')).upper().strip()[0]

    if op == 'P':
        break

print(f'Total de {midade} maiores de idade')
print(f'Total {ho} homens')
print(f'Total {mu} mulheres menor de 18 anos')
