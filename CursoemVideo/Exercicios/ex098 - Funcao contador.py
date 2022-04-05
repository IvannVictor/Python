from time import sleep

def contador(inicio, fim, passos):
    print('=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {passos} em {passos}')

    if passos < 0:  # Vai verificar se passos é negativo e transformar ele em possitivo
        passos = passos * -1

    if passos == 0:  # Vai verificar se passos não é zero e transformar ele em 1
        passos = 1

    if inicio < fim:  # Vai executar enquanto o inicio for maior que o fim
        cont = inicio  # começa no inicio vai ate o fim na quantidade de passos desejadados
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)  # Em versões mais antigas tinha que colocar no final do print flush=True, para fazer a contagem
            cont = cont + passos
        print('Fim')

    else:  # Vai executar enqaunto o fim for maior que o incio
        cont = inicio
        while cont > fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont = cont - passos
        print('Fim')


# Programa principal
contador(1, 10, 1)
contador(10, 1, 1)
print('=' * 20)
contador(int(input('Agora é sua vez\nInicio: ')), int(input('Fim:   ')), int(input('Passos: ')))
