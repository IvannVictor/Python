from random import randint
from operator import itemgetter  # usada para contar itens dos dicinarios
from time import sleep

jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}

print('Resultado das jogas de cada um')
for j, i in jogo.items():
    print(f'{j} tirou {i}')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # Comando usado para montar a lista invertida

print()
print('-=' * 17)
print(f'{"-= Ranking =-":-^33}')

for i, r in enumerate(ranking):  # Quando usamos o itemgetter ele transforma os dicionarios em lista
    print(f'Em {i + 1}º lugar ficou: {r[0]} com {r[1]}')
    sleep(1)
print(f'{"-= Bons jogos =-":-^33}')
