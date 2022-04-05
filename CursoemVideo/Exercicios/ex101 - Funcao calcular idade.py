def voto(nasc):
    """
    -> Função usada para verificar se o usuario esta na idade de votar ou não
    :param nasc: Recebe o ano de nascimento
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 18:
        print(f'Voce tem somente {idade}, ainda não precisa votar')
    elif idade < 65:
        print(f'Com {idade} anos, seu voto é obrigatorio')
    elif idade >= 65:
        print(f'Na sua idade de {idade} anos, voce tem o voto opcional')


help(voto)
voto(int(input('Digite o ano de nascimento: ')))
