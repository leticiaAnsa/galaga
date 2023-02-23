import pygame
from pygame.locals import *
from sys import exit
from time import sleep

pygame.init()

LARGURA, ALTURA = 225,225
largura,altura = 100,100

tela = pygame.display.set_mode((1000, 700))
tela_1 = pygame.display.set_caption('GALAGA')

#player
player = pygame.image.load('player_1.png')
player = pygame.transform.scale(player, (LARGURA, ALTURA))

player_x = 400
player_y = 400

#nave inimiga 1
nave_1 = pygame.image.load('nave.png')
nave_1 = pygame.transform.scale(nave_1, (80,80))


#nave inimiga 2
nave_2 = pygame.image.load('nave.png')
nave_2 = pygame.transform.scale(nave_2, (80,80))


#nave inimiga 3
nave_3 = pygame.image.load('nave.png')
nave_3 = pygame.transform.scale(nave_3, (80,80))


#lazer
lazer = pygame.image.load('lazer_1.png')
lazer = pygame.transform.scale(lazer, (50, 50))

lazer_x = 487
lazer_y = 350

while True: 
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit
            exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player_x = player_x + 20
                lazer_x = lazer_x + 20
            if event.key == K_LEFT:
                player_x = player_x - 20
                lazer_x = lazer_x - 20
            if event.key == K_UP:
                player_y = player_y - 20
                lazer_y = lazer_y - 20
            if event.key == K_DOWN:
                player_y = player_y + 20
                lazer_y = lazer_y + 20
            if event.key == K_a:
                sleep(0.5)
                tela.blit(lazer, (lazer_x, lazer_y))

    tela.blit(player,(player_x, player_y))
    tela.blit(nave_1,(480,30))
    tela.blit(nave_2,(345,30))
    tela.blit(nave_3,(600,30))
    # tela.blit(lazer,(lazer_x, lazer_y))


    pygame.display.update()




 








