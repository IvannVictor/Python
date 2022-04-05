maior = 0
menor = 0
for c in range(1,6):
    peso =  float(input('Digite o peso da {}º pessoa '.format(c)))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso é {}Kg e o menor peso é {}Kg'.format(maior, menor))
