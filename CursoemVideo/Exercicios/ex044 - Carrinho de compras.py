from time import sleep

print('\033[33m=-\033[m' * 30)
print('{} {:=^60} {}'.format('\033[36m', 'LOJA IVAN', '\033[m'))
print('\033[33m=-\033[m' * 30)

valor = float(input('Digite o valor do produto R$'))
print('''Qual vai ser a forma de pagamento?
[ 1 ] À VISTA DINHEIRO/CHEQUE 
[ 2 ] À VISTA CARTÃO
[ 3 ] 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO''')
op = int(input('Qual a sua opção? '))

if op == 1:
    pre = valor - (valor * 10 / 100)
    print('O valor que voce ira pagar é R${:.2f}'.format(pre))
elif op == 2:
    pre = valor - (valor * 5 / 100)
    print('Voce ira pagar R${:.2f}'.format(pre))
elif op == 3:
    pre = valor / 2
    print('Voce ira pagar 2 parcelas de R${:.2f}'.format(pre))
elif op == 4:
    par = int(input('Quantas parcelas? '))
    pre = valor + (valor * 20 / 100)
    total = pre / par
    print('Voce ira parcelar em {}x pagando o valor de R${:.2f} e ficando o valor final de {:.2f}'.format(par, total, pre))
