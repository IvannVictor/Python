from time import sleep

dados = dict()
pessoas = list()
soma =  idade = 0

while True:
    dados["Nome"] = str(input('Digite o nome: ')).strip().title()
    dados["Idade"] = int(input('Digite a idade: '))
    soma = soma + dados["Idade"]
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Digite o sexo (F/M) ')).strip().upper()[0]
        if sexo not in 'FM':
            print('Por favor, digite F ou M')
            sleep(0.5)
    dados["Sexo"] = sexo
    pessoas.append(dados.copy())  # comando para copiar o dicionario para a lista

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? (S/N)')).strip().upper()[0]
        if op not in 'SN':
            print('Por favor, digite apenas S ou N')
            sleep(1)

    if op == 'N':
        break

print()
print(f'O total de pessoas é {len(pessoas)}')
media = soma / len(pessoas)
print(f'A media das idade é {media:.2f} anos')
print('O nome das mulheres cadastradas foram:', end=' ')
for p in pessoas:
    if p["Sexo"] == 'F':
        print(f'{p["Nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da media:', end=' ')
for p in pessoas:
    if p["Idade"] > media:
        print('       ')
        for i, k in p.items():
            print(f'{i} = {k}', end=' ')
print()
