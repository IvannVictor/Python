palavras = ('Pao', 'Arroz', 'Peixe', 'Paralelepipedo')

for p in palavras:
    print(f'\nNa palavra "{p}" temos: ', end=' ')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
