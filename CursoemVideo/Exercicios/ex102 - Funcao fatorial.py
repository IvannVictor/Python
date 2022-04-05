def factorial(nun, show=False):
    """
    -> Calcula o fatorial de um numero
    Factorial é multiplocar o valores pelos numeros menores a ele ate o 1
    : param nun: O valor
    : param show: Caso queira ver os valores que foram multiplicados
    : return: Retorna o valor do fatorial
    """
    f = 1
    for c in range(nun, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f = f * c
    return f


help(factorial)
print(factorial(5))
print(factorial(5, True))
