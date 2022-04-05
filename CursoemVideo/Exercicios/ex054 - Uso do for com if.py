from datetime import date

atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 4):
    nas = int(input('Digite o ano de nascimento da {}º pessoa '.format(c)))
    idade = atual - nas
    if idade <21:
        totalmenor = totalmenor + 1

    else:
        totalmaior = totalmaior +1

print('Tem o total de {} menor de idade'.format(totalmenor))
print('Tem o total de {} maior de idade'.format(totalmaior))