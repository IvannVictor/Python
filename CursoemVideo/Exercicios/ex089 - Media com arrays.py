ficha = list()

while True:  # Primeiro vai receber os dados e analisar, depois armazenar na lista
    nome = str(input('Digite o nome: ')).strip().title()
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja cadastrar mais alunos? (S/N)')).upper().strip()[0]
    if op == 'N':
        break

print('-=' * 11)
print(f'{"Nº":<4}{"Nome":<10}{"Media":>8}')
print('-=' * 11)

for i, f in enumerate(ficha):
    print(f'{i:<4}{f[0]:<10}{f[2]:>8}')
print('-=' * 11)

while True:
    op = int(input('Mostrar as notas de qual aluno? (Digite 999 para finalizar) '))

    if op == 999:
        print('Finalizando........')
        break

    if op <= len(ficha) - 1:
        print(f'\nAs notas de {ficha[op][0]}, é {ficha[op][1]}')  # OP ecolhe a pessoa e 0 e 1 são o nome da OP e as notas

print('Volte sempre!❤')
