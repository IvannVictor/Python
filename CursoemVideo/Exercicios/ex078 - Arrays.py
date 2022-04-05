valores = []
maior = 0
menor = 0
for pos in range(0, 5):
    valores.append(int(input(f'Digite o valor que vai na posição {pos}: ')))

    if pos == 0:
        maior = menor = valores[pos]
    else:
        if valores[pos] > maior:
            maior = valores[pos]

        if valores[pos] < menor:
            menor = valores[pos]

print('\n-=' * 35)
print(f'A lista de valore digitada foi {valores}')
print(f'O maior valor é o {maior} e foi digitado na posiçao', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f' {i}', end=' ')

print(f'\nO menor valor é o {menor} e foi digitado na posição', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}', end=' ')
print('\n-=' * 35)

print('\nObrigado por participar😊😊')
