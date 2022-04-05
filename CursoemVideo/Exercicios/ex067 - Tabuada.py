print('=' * 30)
print('Calculadora da multiplicação')
print('=' * 30)

while True:
    v = int(input('\nValor '))
    if v < 0:
        break
    for c in range(0, 11):
        m = c * v
        print(f'{v} * {c} = {m}')
print('Tabuada encerrada, obrigado por participar')
