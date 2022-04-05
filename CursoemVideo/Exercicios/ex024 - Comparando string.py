n1 = input('Vamos validar\nDigite o nome da sua cidade ').strip()
n1 = n1.title()
div = n1.split()
print('A sua cidade começa com "Santo"? {}'.format('Santo' in div[0]))


print('Correção/outra alternativa')
print('A sua cidade começa com "Santo"? {}'.format(n1[:5] == 'Santo'))
