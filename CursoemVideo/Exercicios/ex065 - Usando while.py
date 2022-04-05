c = 0
op = ''
so = 0
maior = 0
meor= 0

while op != 'P':
    v = int(input('Digite um valor'))
    op = str(input('Deseja colocar mais? [s/p]')).upper().strip()
    c = c + 1
    so = so + v
    media = so / c
    if c == 1:
        maior = meor = v
    else:
        if v > maior:
            maior = v
        if v < meor:
            meor = v
print(f'Voce digitrou {c} valores, a media deles é de {media}')
print('O maior valor é {} e meor é {}'.format(maior, meor))
