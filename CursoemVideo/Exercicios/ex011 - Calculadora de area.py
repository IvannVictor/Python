n1 = float(input('Vamos descobrir quanto de tinta precisa para pintar um parede\nDigite a altura da parede '))
n2 = float(input('Digite a largura da parede '))

print('A area dessa parede é {}m², voce vai precisar de {} litros de tinta para pintar essa parede'
      .format(n1*n2, (n1*n2)/2))
