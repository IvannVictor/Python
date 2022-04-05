import pygame
pygame.init()
pygame.mixer.music.load('semarquivo.mp3')  # Tenha o audio salvo na mesma pasta do projeto para fazer a execucao!
pygame.mixer.music.play()
pygame.event.wait()
print('Vamos reproduzir uma musica')
