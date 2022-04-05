from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib
import pandas

# Fazendo o python ler o arquivo com os contatos em excel.
contatos_df = pandas.read_excel('Enviar.xlsx')  # Aqui vai o nome do arquivo que contem os contatos.

# Fazendo o python abrir o navegador na pagina do whatsapp web.
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# Verificando se o seu whatsapp ja esta aberto.
while len(navegador.find_elements_by_id("side")) < 1:
    sleep(1)

# Com o login feito, vamos consutar a mensgem e enviar
for i, mensagem in enumerate(contatos_df['Mensagem']):
    while len(navegador.find_elements_by_id('side')) < 1:
        sleep(1)
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"Olá {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"

    sleep(5)
    # Apos ter preparado a mensagem, precisamos abri novamente o whatsapp.
    navegador.get(link)
    while len(navegador.find_elements_by_id('side')) < 1:
        sleep(1)
    sleep(5)
    # Apos aberto, vamos fazer o python enviar a mensagem
    navegador.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    sleep(10)
