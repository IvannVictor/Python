import random
from time import sleep

n1 = int(input('Vamos brincar\nDigite um numero entre 0 e 5 e vamos ver se voce acerta qual o PC escolhe\n'
               'Digite o numero: '))
n2 = random.randint(0, 5)

if n1 == n2:
    print('🎊Voce acertou, o numero que o PC escolheu foi {} e voce acertou, PARABENS!!🎉🎊'.format(n2))
else:
    print('Voce errou, o numero que o PC escolheu foi {} e voce colocou {}, aperte CTRL + F5 e tente novamente 😢😢'
          .format(n2, n1))

print('Correção do exercicio acima 👆')
sleep(2)
print('=-'*30)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('=-'*30)
print('Processando......')
sleep(2)
if n1 == n2:
    print('🎊Parabens, voce conseguiu me vencer🎊')
else:
    print('😝Ganhei, eu pensei em {} e não em {}😝'.format(n2, n1))
