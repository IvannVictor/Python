'''
sexo = ' '
while sexo != "":
    sexo = str(input('Digite o sexo [M/F] ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Por favor digite um sexo valido')
    else:
        print('Sexo {}, registrado com sucesso'.format(sexo))
        exit()
'''

sexo = str(input('Digite seu sexo [M/] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Por favor, digite um sexo valido '))
print('Sexo {}, registrado'.format(sexo))
