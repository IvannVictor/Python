from time import sleep
from lib.interface import *
from lib.arquivo import *

arg = 'cursoemvideo.txt'
if not arquivoExiste(arg):
    criarArquivo(arg)

while True:
    resposta = menu(['Ver usuarios cadastradas', 'Cadastrar novo usuario', 'Sair do sistema'])

    if resposta == 1:
        # Ler os dados do aquivo
        leiaArquivo(arg)
    elif resposta == 2:
        cabeçalho('CADASTRO DE PESSOAS')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arg, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema.... Ate logo 😁')
        break
    else:
        print('\033[31mPor favor, escolha uma opção valida\033[m')
    sleep(2)
