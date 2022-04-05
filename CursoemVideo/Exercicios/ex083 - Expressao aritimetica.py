expressão = str(input('Digite uma expressão aritinetica: '))
parentessesaberto = []
parentessesfechado = []

for e in expressão:
    if e == '(':
        parentessesaberto.append('(')

    elif e == ')':
        parentessesfechado.append(')')

if len(parentessesfechado) == len(parentessesaberto):
    print('Essa expressão é valida')
else:
    print('Essa expressão é invalida!')
