from tkinter import *
from PIL import Image, ImageTk  # Biblioteca para mexer com imagens
import speedtest  # Biblioteca para medir a velocidade


# Medindo a velocidade!
def medir():
    speed = speedtest.Speedtest()
    down = f"{'{:.2f}'.format(speed.download() / 1024 / 1024)}"
    up = f"{'{:.2f}'.format(speed.upload() / 1024 / 1024)}"

    # Alterando nos labels
    ldown['text'] = down
    lup['text'] = up

    # Mudando o botao
    btn['text'] = 'TESTAR NOVAMENTE'
    btn.place(x=115, y=100)


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
janela.geometry("350x200")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

# Dois frames
frameLogo = Frame(janela, width=350, height=60, bg=cor3)
frameLogo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frameCorpo = Frame(janela, width=350, height=140, bg=cor3)
frameCorpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando o frame logo
imagem = Image.open('IMG\speed100px.png')
imagem = imagem.resize((55,55))
imagem = ImageTk.PhotoImage(imagem)

lLogo = Label(frameLogo, height=60, image=imagem, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=cor3, fg= cor4)
lLogo.place(x=20, y=0)

lNome = Label(frameLogo,text='Internet speed test', height=60, compound=LEFT, padx=10, anchor='nw', font=('Ivy 20 bold'), bg=cor3, fg= cor1)
lNome.place(x=75, y=10)

lLinha = Label(frameLogo,width=350, anchor=NW, font=('Ivy 1 bold'), bg=cor4, fg= cor1)
lLinha.place(x=0, y=59)

# Configurando frame corpo
# Down
ldown = Label(frameCorpo,text='', height=60, compound=LEFT, anchor=NW, font=('Arial 28'), bg=cor1, fg=cor3)
ldown.place(x=44, y=25)

ldownr = Label(frameCorpo,text='Mbps Download', height=60, compound=LEFT, anchor=NW, font=('Ivy 10'), bg=cor3, fg=cor1)
ldownr.place(x=30, y=70)

imgDown = Image.open('IMG\DOWN30px.png')
imgDown = imgDown.resize((50,50))
imgDown = ImageTk.PhotoImage(imgDown)
limgDown = Label(frameCorpo, height=60, image=imgDown, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=cor3, fg= cor4)
limgDown.place(x=130, y=30)

# Up
lup = Label(frameCorpo,text='', height=60, compound=LEFT, anchor=NW, font=('Arial 28'), bg=cor1, fg=cor3)
lup.place(x=235, y=25)

lupr = Label(frameCorpo,text='Mbps Upload', height=60, compound=LEFT, anchor=NW, font=('Ivy 10'), bg=cor3, fg=cor1)
lupr.place(x=235, y=70)

imgUp = Image.open('IMG\CIMA30px.png')
imgUp = imgUp.resize((50,50))
imgUp = ImageTk.PhotoImage(imgUp)
limgUp = Label(frameCorpo, height=60, image=imgUp, compound=LEFT, padx=10, anchor='nw', font=('Ivy 16 bold'), bg=cor3, fg= cor4)
limgUp.place(x=170, y=30)

# Botao
btn = Button(frameCorpo,text='INICIAR TESTE',command=medir, font=('Ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor1, fg=cor3)
btn.place(x=135, y=100)

# manter o janela aberta
janela.mainloop()