n1 = input('Vamos separar\nDigite seu nome completo ').strip()
n1 = n1.title()
div = n1.split()
print('''Seu nome comleto é {}
Seu primeiro nome é {}
Seu ultimo nome é {}'''.format(n1, div[0], div[-1:]))

print('Correção')
print('Seu nome comleto é {}'.format(n1))
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu ultimo nome é {}'.format(div[len(div)-1]))
