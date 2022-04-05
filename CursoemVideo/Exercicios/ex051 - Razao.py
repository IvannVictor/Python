n1 = int(input('Primeiro valor: '))
razao = int(input('Razao: '))
decimo =n1 + (10 - 1) * razao

for c in range(n1, decimo + razao, razao):
    print(c)