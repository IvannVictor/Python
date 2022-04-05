from time import sleep

v1 = int(input('Digite o 1º valor: '))
v2 = int(input('Digite o 2º valor: '))
opcao = 0

while opcao !=5:
    sleep(2)
    print('''\n    [ 1 ] Para somar
    [ 2 ] Para multiplicar
    [ 3 ] Para maior entre eles
    [ 4 ] Para novos valores
    [ 5 ] Para fechar o programa''')
    print('>'*10)

    opcao = int(input('Qual a sua opção: '))

    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} e {} = {}'.format(v1, v2, soma))
    elif opcao == 2:
        produto = v1 * v2
        print('O produto da multiplicação entre {} e {} é {}'.format(v1, v2, produto))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior é {}'.format(maior))
    elif opcao == 4:
        v1 = int(input('Digite o 1º valor: '))
        v2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('Fializando....')
    else:
        print('Por favor, digite uma opçao valida')

sleep(2)
print('Foi um prazer ter voce aqui!! Volte sempre.')
