def dobro(nun):
    res = nun * 2
    return res


def metade(nun):
    res = nun / 2
    return res


def aumentando(nun, taxa):
    res = nun + (nun / 100 * taxa)
    return res


def diminuir(nun, taxa):
    res = nun - (nun / 100 * taxa)
    return res


def formatação(pre=0, moeda='R$'):
    return f'{moeda}{pre:.2f}'.replace('.', ',')
