matrixz = [[], [], []]

print('Digite os valores para serem preenchidos na matriz')
for v in range(1, 10):
    va = int(input(f'{v}º valor: '))

    if v <= 3:
        matrixz[0].append(va)

    if 7 > v >= 4:
        matrixz[1].append(va)

    if v >= 7:
        matrixz[2].append(va)

print()
print(matrixz[0])
print(matrixz[1])
print(matrixz[2])
