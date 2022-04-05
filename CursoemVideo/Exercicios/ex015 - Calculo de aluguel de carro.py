n1 = int(input('Vamos calcular quanto voce ira pagar no alugal do carro\nQuantos dias passou com o carro? '))
n2 = float(input('Quantos KM foram percorridos nesses {} dias que voce esteve com o carro? '.format(n1)))
pd = n1*60
pk = n2*0.15
r = pd+pk

print('O valor a ser pago pelo aluguel do caro é de R${}'.format(r))
