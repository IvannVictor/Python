def dobro(nun, formatado=False):
    res = nun * 2
    return res if formatado is False else formatação(res)


def metade(nun, formatado=False):
    res = nun / 2
    return res if formatado is False else formatação(res)


def aumentando(nun, taxa, formatado=False):
    res = nun + (nun / 100 * taxa)
    return res if formatado is False else formatação(res)


def diminuir(nun, taxa, formatado=False):
    res = nun - (nun / 100 * taxa)
    return res if formatado is False else formatação(res)


def formatação(pre=0, moeda='R$'):
    return f'{moeda}{pre:.2f}'.replace('.', ',')


def resumo(pre=0, taxa=10, tx=10):
    print('-' * 36)
    print('RESUMO DO VALOR'.center(36))
    print('-' * 36)
    print(f'O valor analisasdo foi: \t{formatação(pre)}')  # \t Adiciona espaço para formatação
    print(f'O dobro do valor é: \t\t{dobro(pre, True)}')
    print(f'A metade do valor é: \t\t{metade(pre, True)}')
    print(f'O desconto de {taxa} é: \t\t{diminuir(pre, taxa, True)}')
    print(f'O aumento de {tx} é: \t\t\t{aumentando(pre, tx, True)}')
    print('-' * 36)
