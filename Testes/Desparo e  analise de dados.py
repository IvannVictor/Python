import pandas as pd
import win32com.client as win32

# Importar a base de dados
tabela_venda = pd.read_excel('planilhas\Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)

# Faturamento por loja
faturamento = tabela_venda[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()

# Quantidade de produtos vendidos por loja
produtos_vendidos = tabela_venda[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()

# Ticket medio dos produtos por loja
ticket_medio = (faturamento['Valor Final'] / produtos_vendidos['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})

# Enviar um e-mail com o relatorio
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'iivanvictor@outlook.com;'
mail.Subject = 'Relatorio de vendas'
mail.HTMLBody = f'''
Caros,

<p>Segue o relatorio de vendas das empresas</p>

<p>Faturamento</>
{faturamento.to_html(formatters={'Valor Final': f" {'R$':,.2f}"})}# Para enviar retirar essa formatação, esta com erro

<p>Quantidade de produtos vendidos por loja</p>
{produtos_vendidos.to_html()}

<p>Ticket medio dos produtos por loja</p>
{ticket_medio.to_html(formatters={'Ticket Médio': f' {"R$":,.2f}'})}

<p>Att.</p>

<p>Ivan Victor</p>
<p>Tecnico de informatica</p>
<p>iivanvictor@outlook.com</p>
'''
mail.Send()
print('E-mail enviado com sucesso. Confira sua caixa de entrada!!')
