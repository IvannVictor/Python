soma = 0
cont = 0
for par in range(1, 501, 2):
    if par % 3 == 0:
        cont = cont +1
        soma += par
print('A soma de todos os {} valores da o total de {}'.format(cont, soma))
