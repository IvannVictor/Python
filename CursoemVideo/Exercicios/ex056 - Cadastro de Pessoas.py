somaidade = 0
meidaidade = 0
maioridadem = 0
nomevelho = ''
totalmv = 0

for p in range(1, 5):
    print('====={}º pessoa====='.format(p))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F] ')).strip().upper()
    somaidade = somaidade + idade

    if p == 1 and sexo == 'M':
        maioridadem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadem:
        maioridadem = idade
        nomevelho = nome

    if sexo == "F" and idade < 20:
        totalmv = totalmv + 1

meidaidade = somaidade / 4
print('A media de idade é {}'.format(meidaidade))
print('O homem mais velho se chama {} e tem a idade de {} anos'.format(nomevelho, maioridadem))
print('No grupo possui {} mulheres abaixo de 20 anos'.format(totalmv))
