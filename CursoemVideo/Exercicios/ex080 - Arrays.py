valores = list()

for c in range(0, 5):
    n = int(input('Digite um numero: '))

    if c == 0 or n > valores[-1]:
        valores.append(n)
        print(f'O valor {n}, foi adicinado ao final da lista')
    else:
        pos = 0
        while pos != len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'O valor {n}, foi adicinado na posição {pos}')
                break
            pos = pos + 1

print(f'A sua lista ficou dessa forma {valores}')
