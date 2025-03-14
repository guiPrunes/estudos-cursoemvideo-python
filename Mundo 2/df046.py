# CONTAGEM REGRESSIVA COM FOGOS
# CUIDADO COM O BARULHO

from time import sleep
import pygame
print('Vamos estourar fogos de artificio, escolha a contagem...')
c = int(input('Digite um valor para contagem regressiva: '))
for c in range(c, 0, -1):
    print(c)
    sleep(1)
print("boom")
pygame.init()
pygame.mixer.music.load('fogos.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())
