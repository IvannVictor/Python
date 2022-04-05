jogador = {}
gols = []
c = 0

jogador["Nome"] = str(input('Nome do jogador?: ')).strip().title()
quant = int(input('Quantos jogos teve? '))
for c in range(1, quant + 1):
    gols.append(int(input(f'Quantos gols teve na {c}ª partida? ')))
jogador["Gols"] = gols[:]  # nunca esquecer o [:]
jogador["total"] = sum(gols)  # Sum usado para somar os numeros na lista

print()
print('-=' * 30)
print(jogador)

print()
for i, j in jogador.items():
    print(f'{i} = {j}')

print()
print(f'Jogador {jogador["Nome"]} jogou {quant} jogos')
for i, n in enumerate(gols):
    print(f'Na {i + 1}ª partida o {jogador["Nome"]} fez o total de {n} gols')
print(f'Total de {jogador["total"]} gols')
