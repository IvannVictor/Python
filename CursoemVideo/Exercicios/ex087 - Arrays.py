matrixz = [[], [], []]
somapar = somacolum3 = maiorvalorseglin = 0

print('Digite os valores para serem preenchidos na matriz')
for v in range(1, 10):
    va = int(input(f'{v}º valor: '))

    if v <= 3:
        matrixz[0].append(va)

    if 7 > v >= 4:
        matrixz[1].append(va)

    if v >= 7:
        matrixz[2].append(va)

    if va % 2 == 0:
        somapar = somapar + va

somacolum3 = matrixz[0][2] + matrixz[1][2] + matrixz[2][2]  # Somando os valores finais de cada lista dentro da lista
maiorvalorseglin = max(matrixz[1])  # Analisando o maior valor da segunda lista

print()
print(matrixz[0])
print(matrixz[1])
print(matrixz[2])

print()
print(f'A soma dos valores pares é: {somapar}')
print(f'A soma dos valores da 3º coluna é: {somacolum3}')
print(f'O maior valor da segunda linha é: {maiorvalorseglin}')
