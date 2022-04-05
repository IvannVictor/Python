def maior(*nun):  # O * serve para o python entender que vai receber varios valores
    maior = cont = 0
    print('=' * 40)
    print('\nAnalisando os valores informados...')

    for valores in nun:
        print(f'{valores}', end=' ')
        cont = cont + 1

        if cont == 0:  # para a verificação funcionar, ela tem que esta dentro do for
            maior = valores
        else:
            if valores > maior:
                maior = valores

    print(f'Foram informados {cont} numeros ao todo')
    print(f'\nO maior encontrado foi o {maior}')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 34, 65, 12, 34, 5, 65, 6, 787, 33, 988, 54, 332, 2345, 76, 8, 97)
maior(1, 3, 5, 6, 8, 0)
maior(9)
maior(0)
