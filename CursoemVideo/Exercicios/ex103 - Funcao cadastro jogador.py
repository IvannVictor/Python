def jogador(nome='<Desconhecido>', gols=''):

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Digite o nome do Jogador: ')).title()
g = str(input(f'Digite a quantidade de gols que o jogador {n} fez no campeonato: '))

if g.isnumeric():  # Verifica se pode ser numerico o que foi digitado no texto
    gols = int(g)
else:
    gols = 0

if n.strip() == '':
    jogador(gols=g)
else:
    jogador(n, g)
