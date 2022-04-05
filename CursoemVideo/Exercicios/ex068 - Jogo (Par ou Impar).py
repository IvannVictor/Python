from random import randint

print('=' * 30)
print('Vamos jogar,Par ou Impar')
print('=' * 30)

c = 0
p = 'Par'
i = 'Impar'
while True:

    pc = randint(0, 10)
    v = int(input('Digite um valor: '))
    s = v + pc
    r = s % 2
    op = ' '

    while op not in 'IP':
        op = str(input('Par ou Impar? [P/I] ')).upper().strip()

    if r == 0:
        print(f'O pc escolheu {pc} e a soma com o seu da {s}, o valor é {p}')
        if op == 'P':
            print('Acertou')
            c = c + 1
        else:
            print('Errou')
            break

    elif r == 1:
        print(f'O pc escolheu {pc} e a soma com o seu da {s}, o valor é {i}')
        if op == 'I':
            print('Acertou')
            c = c + 1
        else:
            print('Errou')
            break

if c == 1:
    print('Voce acertou uma vez')

else:
    print(f'Voce acertou {c} vezes')
