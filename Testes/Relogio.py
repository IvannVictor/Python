from tkinter import *
from datetime import datetime
# OBS: voce pode baixar a biblioteca pyglet para adicionar mais fonts

# Cores usadas
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

# Fundo
fundo = cor1
cor = cor2  # letra

# Criadno a janela!
janela=Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


# Criando a funcao para pegar o dados da data e hora
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    diaSemana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    # Colocando os resultado no label
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=diaSemana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))


# Interface
l1 =  Label(janela, text="", font=("Arial 80"), bg=fundo, fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("Arial 20"), bg=fundo, fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)
relogio()

# manter o janela aberta
janela.mainloop()