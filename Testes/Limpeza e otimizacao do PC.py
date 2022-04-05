# Este programa foi feito com base nas dimensoes da minha tela, por favor, acessar o programa "Colotor de posicao do mouse" para atualizar o pontos onde fica os programas em seu PC
from time import sleep
import pyautogui
import pyperclip

# Pausa para cada execução
pyautogui.PAUSE = 1

# Acessar o executar e acessar a pasta temp
pyautogui.hotkey('win', 'r')
pyperclip.copy('temp')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Apagar os dados da pasta temp
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
sleep(5)
pyautogui.click(x=549, y=295)  # Nao esqueca de colocar o posicionamento do seu ponteiro do mouse para nao dar erro e haver, caso necessario coloque mais linha de comando. 
pyautogui.click(x=735, y=322)
sleep(3)
pyautogui.click(x=735, y=322)
pyautogui.hotkey('ctrl', 'w')

# Acessar o executar e acessar a pasta %temp%
pyautogui.hotkey('win', 'r')
pyperclip.copy('%temp%')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Apagar os dados da pasta %temp%
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
sleep(5)
pyautogui.click(x=549, y=295)
pyautogui.click(x=735, y=322)
sleep(3)
pyautogui.click(x=735, y=322)
pyautogui.hotkey('ctrl', 'w')

# Acessar o executar e acessar a pasta prefetch
pyautogui.hotkey('win', 'r')
pyperclip.copy('prefetch')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
pyautogui.press('enter')

# Apagar os dados da pasta prefetch
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
sleep(5)
pyautogui.click(x=549, y=295)
pyautogui.click(x=735, y=322)
sleep(3)
pyautogui.click(x=735, y=322)
pyautogui.hotkey('ctrl', 'w')

# Acessar o executar e acessar a pasta recent
pyautogui.hotkey('win', 'r')
pyperclip.copy('recent')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Apagar os dados da pasta recent
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
sleep(5)
pyautogui.click(x=549, y=295)
pyautogui.click(x=735, y=322)
sleep(3)
pyautogui.click(x=735, y=322)
pyautogui.hotkey('ctrl', 'w')

# Acessar o executar e acessar a pasta cleanmgr
pyautogui.hotkey('win', 'r')
pyperclip.copy('cleanmgr')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Apagando os dados de arquivos mortos
sleep(2)
pyautogui.click(x=755, y=745)
sleep(2)
pyautogui.press('enter')
pyautogui.press('enter')

# Acessando o cmd
pyautogui.press('win')
pyperclip.copy('cmd')
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy('chkdsk c:/f')
pyautogui.click(x=275, y=198, button='right')
pyautogui.press('down')
pyautogui.press('enter')
