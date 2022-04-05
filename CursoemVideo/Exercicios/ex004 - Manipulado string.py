txt = input('Digite qualquer coisa ')

print('O tipo primitivo é', type(txt))
print('Só tem espaço?', txt.isspace())
print('É alfabetico? ', txt.isalpha())
print('É alfanumerico? ', txt.isalnum())
print('Esta em maiuscula? ', txt.isupper())
print('Esta em minuscula?', txt.islower())
print('Esta capitalizada? ', txt.istitle())

print('Usando a sinteze .format')

print('O tipo primitivo é {}'.format(type(txt)))
print('Só tem espaço? {}'.format(txt.isspace()))
print('O tipo primitivo é {}, usa espaço somente? {}. Esta capitalizado(Primeira letra maiuscula) {}'
      .format(type(txt), txt.isspace(), txt.istitle()))
