n1 = float(input('Digite a velocidade atual: '))
n2 = (n1 - 80) * 7
if n1 <= 80:
    print('Cuidado com o limite de velocidade dessa via que 80 KM, sua valocidade atual é de {}'.format(n1))
else:
    print('Voce esta acima do limite de velocidade, voce esta sendo multado em R${:.2f}'.format(n2))
