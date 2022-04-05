n1 = input('Vamos contar caracteres\nDigite seu nome completo: ').strip()
n1 = n1.title()
div = n1.split()
print('''Seu nome com todas as letras maiusculas fica assim: {}
Seu nome com todas as letras minusculas fica assim: {}
Seu nome com cada inicial maiuscula fica assim {}
Seu primeiro nome {} tem {} letras
Seu nome tem {} letras'''
      .format(n1.upper(), n1.lower(), n1.title(), div[0], len(div[0]), len(n1.replace(' ', ''))))
