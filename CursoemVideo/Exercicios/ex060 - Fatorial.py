v = int(input('Digite o valor que quer ver o fatorial '))
c = v
f = 1

print('{}! '.format(v), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print(f)
