print('-='*30)
print('ada'*20)
print('-='*30)

c = 0
s = 0
m = 0

while True:
    v = int(input('Digite um valor [ 0 parar ]: '))
    c = c + 1
    s = s + v
    m = s / c
    if v == 0:
        break
print(f'Voce digitou o total de {c}, a media deles é de {m:.2f} e a soma {s}')
print('Muito origado por participar')
