jogador = {}
gols = []
time = []

# Armazenar os dados
while True:
    jogador["Nome"] = str(input('Nome do jogador?: ')).strip().title()
    quant = int(input('Quantos jogos teve? '))
    gols.clear()
    for c in range(1, quant + 1):
        gols.append(int(input(f'Quantos gols o jogador {jogador["Nome"]} teve na {c}ª partida? ')))
    jogador["Gols"] = gols[:]  # nunca esquecer o [:]
    jogador["total"] = sum(gols)  # Sum usado para somar os numeros na lista
    time.append(jogador.copy())

    # Se vai colocar mais jogadores
    while True:
        op = str(input('Deseja cadastrar mais jogadores? (S/N)')).upper().strip()[0]
        if op not in 'SN':
            print('Por favor, colocar S ou N')
        if op in 'SN':
            break
    if op == 'N':
        break
    print()

# Mostrar os dados dos jogadores
print()
print('Cod.', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')  # Vai mostrar o cabeçalho
print()

print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-'*40)

# Mostra os dados individualmente
print()
while True:
    busca = int(input('Digite o codigo do jogador que voce gostari de analisar (999 encerra o progorama) '))
    if busca == 999:
        break

    if busca >= len(time):  # Verifica se não é maior que a lista de jogadores
        print(f'Não existe jogador no codigo {busca}')

    else:  # Mostra os dados dos jogadores individualmente
        print(f'----- Dados do jogador {time[busca]["Nome"]}-----')

        for n, g in enumerate(time[busca]["Gols"]):  # Para cada partida mostra a quantidade de gols
            print({f'    Na {n + 1}ª partida fez {g} gols'})
    print('-'*30)
print('<<<<<<< Volte sempre >>>>>>>')
