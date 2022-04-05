def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mPor favor digite um numero inteiro valido\033[m')
            continue  # Usado para voltar para o while
        except KeyboardInterrupt:
            print('\n\033[31mProgama finalizado pelo usuario')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[33mPor favor coloque um numero real\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[33mSistema interrompido pelo usuario')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o valor real foi o {n2}')
