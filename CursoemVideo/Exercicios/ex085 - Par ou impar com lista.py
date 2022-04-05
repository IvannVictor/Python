numeros = [[], []]  # Podemos criar listas dentro de lista

for n in range(1, 8):
    v = int(input(f'Digite o {n}º valor: '))

    if v % 2 == 0:
        numeros[0].append(v)  # Dessa forma adicionamos os valores as listas internas das listas
    else:
        numeros[1].append(v)

numeros[0].sort()
print(f'Os valores pares são esses: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares são esses: {numeros[1]}')
