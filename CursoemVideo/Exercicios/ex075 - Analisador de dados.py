valores = (int(input('Digite um valor ')),
           int(input('Digite outro valor ')),
           int(input('Digite mais um valor ')),
           int(input('Digite o ultimo valor ')))

print(f'O valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'O valor 3 foi digitado na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares são', end=' ')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
