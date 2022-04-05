def leiadinhiro(msg):
    valido = False

    while not valido:
        entrada = input(str(msg))
        if entrada.isalpha():
            print(f'Erro: \"{entrada}\" não é um numero')