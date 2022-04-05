def leiadinhiro(msg):
    valido = False

    while not valido:
        entrada = input(str(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro: \"{entrada}\" não é um numero')
        else:
            return float(entrada)


def leiaint(msg):
    ok = False
    valor = 0

    while True:
        n = str(input(msg))  # recebe aqui mas é solicitado no programa principal
        if n.isnumeric():
            ok = True
            valor = int(n)

        else:
            print('\033[33mErro, por favor digite um numero valido\033[m')

        if ok:
            break
    return valor
