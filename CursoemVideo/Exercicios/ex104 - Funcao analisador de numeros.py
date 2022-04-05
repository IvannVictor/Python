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


n = leiaint('Digite um numero: ')
print(f'O valor que foi digitado é {n}')

