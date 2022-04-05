classificao = ('Palmeiras', 'Atletico - MG', 'Fortaleza', 'Bragantino', 'Atletico - PR', 'Ceara', 'Bahia', 'Fluminence',
               'Flamengo', 'Santos', 'Atletico - go', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional',
               'America - MG', 'Sport Recife', 'Cuiaba', 'Chapecoense', 'Grêmio')

print('\033[34mClassificação Brasileirão 2021\033[m')
print(classificao, '\n')
print(f'Os cinco primeiros são {classificao[:5]}\n')
print(f'Os quatro ultimos são {classificao[-4:]}\n')
print(sorted(classificao), '\n ')
print(f'Chapecoense encotra-se na {classificao.index("Chapecoense")+1}ª posição')
