def notas(*n, sit=False):
    """
    -> Usada para calcular a media e saber a situação do aluno
    :param n: Notas do aluno
    :param sit: Aparece caso voce queira, para aparecer coloque sit=True
    return: Retorna o dicionario
    """

    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'Ruim'

    return r


help(notas)
resp = notas(9, 4, 6, 7, sit=True)
print(resp)
