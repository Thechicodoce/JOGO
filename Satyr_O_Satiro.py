import pygame 
from sys import exit
from random import randint, choice 
from random import random

#Funcoes
def anima_player():
    global player_index

    tela.blit(satiro_parado[int(player_index)], player_rect)
    player_index += 0.1
    if player_index > len(satiro_parado) - 1:
        player_index = 0

def anima_bot():
    pass

def rolagem_dado():
    rolagem_satiro = (randint(0, 20))
    rolagem_bot = (randint(0, 20))

#Inicializa o pygame
pygame.init()

#Variáveis

#Cria a tela
tamanho = (1280, 720)
tela = pygame.display.set_mode(tamanho)

#################################################################################################################

#Importa os arquivos necessarios

#carrega fonte do jogo
fonte_pixel = pygame.font.Font('assets/fonte/PixelType.ttf', 50)

#Plano de fundo
img_fundo = pygame.image.load('assets/fundo/fundo2/ceu.png').convert_alpha()
img_sombra = pygame.image.load('assets/fundo/fundo2/sombra.png').convert_alpha()
img_janela = pygame.image.load('assets/fundo/fundo2/janelas.png').convert_alpha()
img_vela = pygame.image.load('assets/fundo/fundo2/vela.png').convert_alpha()
img_arco = pygame.image.load('assets/fundo/fundo2/arco.png').convert_alpha()
img_chao = pygame.image.load('assets/fundo/fundo2/chao.png').convert_alpha()
img_estatua = pygame.image.load('assets/fundo/fundo2/estatua.png').convert_alpha()

#Altera a escala do plano de fundo
img_fundo = pygame.transform.scale(img_fundo, tamanho)
img_sombra = pygame.transform.scale(img_sombra, tamanho)
img_janela = pygame.transform.scale(img_janela, tamanho)
img_vela = pygame.transform.scale(img_vela, tamanho)
img_arco = pygame.transform.scale(img_arco, tamanho)
img_chao = pygame.transform.scale(img_chao, tamanho)
img_estatua = pygame.transform.scale(img_estatua, tamanho)

#Carrega personagens
player_index = 0
satiro_parado = []
minotauro_parado = []

for imagem in range(1, 13):
    img = pygame.image.load(f'assets/personagem/satiro1/ocio2/ocio2{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    satiro_parado.append(img)

for imagem in range(1, 19):
    img = pygame.image.load(f'assets/personagem/minotauro1/ocio2/ocio2{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    img = pygame.transform.flip(img, True, False)
    minotauro_parado.append(img)

player_rect = satiro_parado[player_index].get_rect(midbottom = (200, 630))
player2_rect = minotauro_parado[player_index].get_rect(midbottom = (1000, 600))

#Altera a escala dos personagens
#satiro_parado = pygame.transform.scale(satiro_parado, 420, 320)

#Define o titulo da janela
pygame.display.set_caption("Satyr - O Sátiro")

#Cria um relogio para controlar o FPS
relogio = pygame.time.Clock()

#################################################################################################################

#Loop
while True:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key ==pygame.K_RIGHT:
                pass

            if evento.key ==pygame.K_LEFT:
                pass

        if evento.type == pygame.KEYUP:
            pass

    #Desenha o fundo na tela
    tela.blit(img_fundo, (0, 0))             
    tela.blit(img_sombra, (0, 0))
    tela.blit(img_janela, (0, 0))
    tela.blit(img_vela, (0, 0))
    tela.blit(img_arco, (0, 0))
    tela.blit(img_chao, (0,0))
    tela.blit(img_estatua, (0,0))

    #Desenha o personagem
    tela.blit(satiro_parado[int(player_index)], player_rect)
    player_index += 0.05
    if player_index > len(satiro_parado):
        player_index = 0

    tela.blit(minotauro_parado[int(player_index)], player2_rect)
    player_index += 0.05
    if player_index > len(minotauro_parado):
        player_index = 0

    #Atualiza a tela com o conteudo
    pygame.display.update()
    
    #Define a quantidade de frames por segundo
    relogio.tick(60)

    #Chama animação do personagens
    anima_player()
    anima_bot()

    #Chama Rolagem de dados
    rolagem_dado

