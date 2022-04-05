from random import randint

valores = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), )

print('Os valores sorteados foram')
for v in valores:
    print(v, end=' ')

print(f'\nO maior valor foi o {max(valores)}')
print(f'O menor valor foi o {min(valores)}')
