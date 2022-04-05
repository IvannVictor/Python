n1 = input('Vamos validar\nDigite uma frase ').strip()
n1 = n1.lower()
print('''Essa frase possui {} letras "A"
A primera letra "A" começa no apos o {}º caracter
A ultima letra "A", aparece apos o {}º caracter'''.format(n1.count('a'), n1.find('a'), n1.rfind('a')))

print('Correção')
print('''Essa frase possui {} letras "A"
A primera letra "A" começa no {}º caracter
A ultima letra "A", aparece no {}º caracter'''.format(n1.count('a'), n1.find('a' + 1), n1.rfind('a' + 1)))
