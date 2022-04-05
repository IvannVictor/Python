cont = 0
c = 0
for soma in range(1, 7):
    n1 = int(input('Digite {}º numero: '.format(soma)))
    if n1 % 2 == 0:
        c = c + 1
        cont = cont + n1
print('O total de numeros pares informado é {} e a soma deles é {}'.format(c, cont))