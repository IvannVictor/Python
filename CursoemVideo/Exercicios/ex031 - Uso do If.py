n1 = float(input('Vamos calcular o valor da viagem\nDigite a distancia: '))
ab = n1*0.50
ac = n1*0.45

if n1 <=200:
    print('Voce vai viajar {}KM e vai pagar R${:.2f}'.format(n1, ab))

else:
    print('Voce vai viajar {}KM e vai pagar R${:.2f}'.format(n1, ac))
