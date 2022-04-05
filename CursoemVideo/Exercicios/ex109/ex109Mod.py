def dobro(nun, formatado=False):
    res = nun * 2
    return res if formatado is False else formatação(nun)


def metade(nun, formatado=False):
    res = nun / 2
    return res if formatado is False else formatação(nun)


def aumentando(nun, taxa, formatado=False):
    res = nun + (nun / 100 * taxa)
    return res if formatado is False else formatação(nun)


def diminuir(nun, taxa, formatado=False):
    res = nun - (nun / 100 * taxa)
    return res if formatado is False else formatação(nun)


def formatação(pre=0, moeda='R$'):
    return f'{moeda}{pre:.2f}'.replace('.', ',')
