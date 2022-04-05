def ajuda(com):  # Função para verificar a biblioteca ou função
    titulo(f'Acessando o manual do mandondo {com}')  # Função usada para personalizar o titulo
    help(com)


def titulo(msg):  # Função para criar o titulo
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


comando = ''
while True:
    titulo('Sistema de ajuda PyHELP')  # função titulo
    comando = str(input('Função ou biblioeteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)  # Função ajuda

titulo('Ate logo')
