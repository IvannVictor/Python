n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
n3 = float(input('Digite um numero: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Com os valores informado é possivel criar um triangulo')
    if n1 == n2 and n2 == n3:
        print('Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Esoceles')
else:
    print('Com os valores informado não é possivel criar um triangulo')
