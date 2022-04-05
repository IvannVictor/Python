from random import randint

compu = randint(0, 10)
jogada = 0
acertou = False

print('Oiii, sou seu computador, pensei em um numero entre 0 e 10, acerta ai')

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    jogada = jogada + 1
    if jogador == compu:
        acertou = True
    else:
        if jogador < compu:
            print('Mais... Vai mais uma vez')
        else:
            print('Menos... Vai outra vez')
print('Voce acertou!!! Pensei {} e voce precisou apenas de {} tentativas'.format(compu, jogada))
