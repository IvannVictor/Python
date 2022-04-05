
from PySimpleGUI import PySimpleGUI as sg

# Layout
from openpyxl.chart import layout

sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha  '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar Login?')],
    [sg.Button('Entrar')]
]

layout2 = [
    [sg.Text('Bem vindo! Esse é somente um prototipo!')],
    [sg.Text('Caso queria deixa alguma sujestão, me mande um e-mail!')]
]
# Janela
janela = sg.Window('Login', layout)
janela2 = sg.Window('Bem Vindo!', layout2)

# Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        if valores['usuario'] == 'adm' and valores['senha'] == '1234':
            janela.close()
            while True:
                eventos, valores = janela2.read()
                if eventos == sg.WINDOW_CLOSED:
                    break
