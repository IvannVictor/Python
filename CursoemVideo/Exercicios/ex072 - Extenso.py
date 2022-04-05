extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:
    va = int(input('Digite um valor entre 0 e 10: '))
    if va <= 10 and va >= 0:
        print(f'O valor que voce digitou foi {va} ele escrito por extenso é {extenso[va]}')

        op = str(input('Deseja contiuar? [S/P] ')).upper().strip()[0]
        while op not in 'SP':
            op = str(input('Por favor, digite "S" para continuar ou "P" para parar ')).upper().strip()[0]

        if op == 'P':
            break
    else:
        print('Errado.', end=' ')
