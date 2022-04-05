from math import sin, cos, tan, radians

n1 = float(input('Vamos descobrir o SENO, COSSENO E TANGENTE\nDigite o angulo '))
seno = sin(radians(n1))
cosse = cos(radians(n1))
tang = tan(radians(n1))
print('O valor do angulo {}º, tem o SENO de {:.2f}\nO valor do angulo {}º, tem o COSSENO de {:.2f}\n'
      'O valor do angulo {}º, tem a TANGENTE de {:.2f}'.format(n1, seno, n1, cosse, n1, tang))
