import pandas as pd

# 1ª Import os dados da tabela
tabela = pd.read_csv(r'planilha.csv')

# 2ª Analizar os dados da tabela
# Remover dados inuteis da tabela
tabela = tabela.drop('nome da celula', axis=1)  # 0 é linha e 1 é coluna

# 3ª Informações sobre a tabela
print(tabela.info())

# Ajustando dados que são numeros para o python entender
tabela['nome da coluna'] = pd.to_numeric(tabela['nome da tabela'], errors='coerce')  # Ignora caso tenha letras

# Apagar colunas vazias e linhas
tabela = tabela.dropna(how='all', axis=1)  # all tudo vazio
tabela = tabela.dropna(how='any', axis=o)  # any que tenha pelo menos um valor vazio

# 4ª Analise exploratoria
print(tabela['Chunr'].values_counts())
print(tabela['Chunr'].values_counts(normalize=True).map('{:.1%}').format)

# 5ª Analisar os dados em grafico, para isso instalar o plotly
import plotly.express as px

for coluna in tabela.columns:  # Para cada coluna na tabela ele gera um grafico
    grafico = px.histogram(tabela, x=coluna, color='Churn')
    grafico.show()
