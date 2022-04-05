def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mPor favor, escolha uma opção valida\033[m')
        except KeyboardInterrupt:
            print('\033[31mUsurio prefere a interrupção do sistema')
            return 3
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[32mMENU PRINCIPAL\033[m')
    c = 1
    for itens in lista:
        print(f'\033[34m{c} - \033[36m{itens}\033[m')
        c = c + 1
    print(linha())
    opc = leiaInt('\033[33mSua opção?\033[m ')
    return opc
