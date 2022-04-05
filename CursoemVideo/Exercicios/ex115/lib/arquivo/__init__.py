from CursoemVideo.Exercicios.ex115.lib.interface import cabeçalho


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # RT read abreviação para ler arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # WR+ write escreve Criar um arquivo de texto
        a.close()
    except:
        print('Arquivo não criado')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def leiaArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';')  # Remove as quebras de linhas
            dado[1] = dado[1].replace('\n', '')  # Trandoforma em lista removendo os separadores de dados
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  # Formatação para mostra bonito
        # print(a.read()) Usado para mostrar tudo sem formatação
    finally:
        a.close()


def cadastrar(arg, nome='desconhecido', idade=0):
    try:
        a = open(arg, 'at')  # AT Append, adiciona dados no texto
    except:
        print('Erro para cadastrar')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Erro para cadastrar a pessoa {nome} no arquivo {arg}')
        else:
            print(f'Pessoa {nome} cadastrada com sucesso')
            a.close()