import pygame 
from sys import exit
from random import randint, choice 
from random import random

#Funcoes
def anima_player():
    global player_index, jogo_ativo
    

    if life_satiro > 0:
        tela.blit(satiro_parado[int(player_index)], player_rect)
        player_index += 0.05
        if player_index > len(satiro_parado) -1:
            player_index = 0
    else:
        tela.blit(satiro_morrer[int(player_index)], player_rect)
        player_index += 0.05
        if player_index > len(satiro_morrer) -1:
            jogo_ativo = 0

        
def andar_player():
    global player_index
    global movimento_satiro, relogio

    player_index = 0

    if not player_rect.colliderect(player2_rect):
        tela.blit(satiro_andar[int(player_index)], player_rect)
        player_index += 0.005
        movimento_satiro += 1
        if player_index > len(satiro_andar) - 1:
            player_index = 0
    else:
        movimento_satiro = 0
        tela.blit(satiro_ataque[int(player_index)], player_rect)
        player_index += 0.005
        if player_index > len(satiro_ataque) - 1:
            tela.blit(satiro_voltar[int(player_index)], player_rect)
            player_index += 0.005
            movimento_satiro -= 5
            if not player_rect == satiro_rect:
                movimento_satiro -= 5
            else:
                movimento_satiro = 0  

        player_rect.x += movimento_satiro          

def anima_bot():
    global player_index
    global movimento_minotauro, jogo_ativo

    if life_bot > 0:
        tela.blit(minotauro_parado[int(player_index)], player2_rect)
        player_index += 0.05
        if player_index > len(minotauro_parado):
            player_index = 0
    else:
        tela.blit(minotauro_morrer[int(player_index)], player2_rect)
        player_index += 0.05
        if player_index > len(minotauro_morrer):
            jogo_ativo = 0
            

def andar_minotauro():
    global player_index
    global movimento_minotauro

    player2_rect.x -= movimento_minotauro
   
    tela.blit(minotauro_parado[int(player_index)], player2_rect)
    player_index += 0.05
    if player_index > len(minotauro_parado):
        player_index = 0
    
    if not player2_rect.colliderect(player_rect):
        tela.blit(minotauro_andar[int(player_index)], player2_rect)
        player_index += 0.005
        movimento_minotauro -= 5
    else:
        movimento_satiro = 0
        tela.blit(minotauro_ataque[int(player_index)], player2_rect)
        player_index += 0.005
        if player_index > len(minotauro_ataque) - 1:
            tela.blit(minotauro_voltar[int(player_index)], player2_rect)
            player_index += 0.005
            movimento_minotauro += 5
            if not player2_rect == bot_rect:
                movimento_minotauro += 5
            else:
                movimento_minotauro = 0 

def rolagem():
    global rolagem_satiro
    global acaotecla
    rolagem_satiro = randint(0, 20)
    
    acaotecla = 0

def rolagem2():
    global rolagem_bot
    rolagem_bot = randint(0, 20)
    
    
    #timer_txt = pygame.USEREVENT + 1
    #pygame.time.set_timer(timer_txt, 5000)

def placar_satiro():
    
    global potion1
    #Muda a cor da opçao se nao exister a possibilidade de agir
    if potion1 <= 0:
        cor_acao2 = '#1A1A1A'
    elif potion1 > 0:
        cor_acao2 = '#FFFFFF'
    
    #Carrega dados do placar Satiro
    txt_life = fonte_pixel.render(f'Vida : {life_satiro}', True, '#D40000')
    txt_potion1 = fonte_pixel.render(f'Potion: {potion1}', True, '#1AD400')
    txt_acao1 = fonte_pixel.render(f'1 - ATACAR', True, '#FFFFFF')
    txt_acao2 = fonte_pixel.render(f'2 - CURAR', True, f'{cor_acao2}')
    txt_dado = fonte_pixel.render(f'Sua rolagem foi: {rolagem_satiro}', True, '#FFFFFF')
    
    tela.blit(txt_dado, (55, 150))
    tela.blit(txt_life, (55,30))
    tela.blit(txt_potion1, (55, 60))
    tela.blit(txt_acao1, (55, 90))
    tela.blit(txt_acao2, (55, 120))
    

def placar_bot():
    txt_life = fonte_pixel.render(f'Vida {life_bot}', True, '#D40000')
    txt_potion2 = fonte_pixel.render(f'Potion: {potion2}', True, '#1AD400')
    txt_dado2 = fonte_pixel.render(f'Rolagem inimiga foi: {rolagem_bot}', True, '#FFFFFF')
    tela.blit(txt_dado2, (940, 150))
    tela.blit(txt_life, (1115,30))
    tela.blit(txt_potion2, (1115, 60))

def acao():
    pass
            
                
def atualizar_jogo():
    pass

# Adicione essas variáveis globais para controlar a velocidade da animação
player_speed = 0.5
bot_speed = 0.5
    

#Inicializa o pygame
pygame.init()

#Variáveis
life_satiro = 100
life_bot = 100
potion1 = 3
potion2 = 1
movimento_satiro = 0
movimento_minotauro = 0
acaotecla = 0
rolagem_satiro = 0
rolagem_bot = 0
jogo_ativo = 1

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
img_placar = pygame.image.load('assets/fundo/fundo2/placar.png').convert_alpha()
img_fim = pygame.image.load('assets/fundo/fundo2/Battleground2.png').convert_alpha()

#Altera a escala do plano de fundo
img_fundo = pygame.transform.scale(img_fundo, tamanho)
img_sombra = pygame.transform.scale(img_sombra, tamanho)
img_janela = pygame.transform.scale(img_janela, tamanho)
img_vela = pygame.transform.scale(img_vela, tamanho)
img_arco = pygame.transform.scale(img_arco, tamanho)
img_chao = pygame.transform.scale(img_chao, tamanho)
img_estatua = pygame.transform.scale(img_estatua, tamanho)
img_placar = pygame.transform.scale(img_placar, (1240, 180))
img_fim = pygame.transform.scale(img_fim, tamanho)

#Carrega personagens
player_index = 0

satiro_parado = []
satiro_ataque = []
satiro_andar = []
satiro_voltar = []
satiro_morrer = []

minotauro_parado = []
minotauro_ataque = []
minotauro_andar = []
minotauro_voltar = []
minotauro_morrer = []

    #Satiro parado
for imagem in range(1, 13):
    img = pygame.image.load(f'assets/personagem/satiro1/ocio2/ocio2{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    satiro_parado.append(img)

    #Satiro andando
for imagem in range(1, 19):
    img = pygame.image.load(f'assets/personagem/satiro1/andar/andar1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420,320))
    satiro_andar.append(img)

    #Satiro voltando
for imagem in range(1, 19):
    img = pygame.image.load(f'assets/personagem/satiro1/andar/andar1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420,320))
    img = pygame.transform.flip(img, True, False)
    satiro_voltar.append(img)

    #Satiro atacando
for imagem in range(1, 13):
    img = pygame.image.load(f'assets/personagem/satiro1/ataque/ataque1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420,320))
    satiro_ataque.append(img)

    #Satiro morrendo
for imagem in range(1, 16):
    img = pygame.image.load(f'assets/personagem/satiro1/morte/morte1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    satiro_morrer.append(img)

    #Minotauro parado
for imagem in range(1, 19):
    img = pygame.image.load(f'assets/personagem/minotauro1/ocio2/ocio2{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    img = pygame.transform.flip(img, True, False)
    minotauro_parado.append(img)

    #Minotauro andando
for imagem in range(1, 25):
    img = pygame.image.load(f'assets/personagem/minotauro1/andar/andar1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    img = pygame.transform.flip(img, True, False)
    minotauro_andar.append(img)

    #Minotauro voltando
for imagem in range(1, 25):
    img = pygame.image.load(f'assets/personagem/minotauro1/andar/andar1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    minotauro_andar.append(img)

    #Minotauro atacando
for imagem in range(1, 13):
    img = pygame.image.load(f'assets/personagem/minotauro1/ataque1/ataque1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    img = pygame.transform.flip(img, True, False)
    minotauro_ataque.append(img)

    #Minotauro morrendo
for imagem in range(1, 16):
    img = pygame.image.load(f'assets/personagem/minotauro1/morte/morte1{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (420, 320))
    img = pygame.transform.flip(img, True, False)
    minotauro_morrer.append(img)

player_rect = satiro_parado[player_index].get_rect(midbottom = (200, 630))
satiro_rect = satiro_parado[player_index].get_rect(midbottom = (200, 630))
player2_rect = minotauro_parado[player_index].get_rect(midbottom = (1000, 600))
bot_rect = minotauro_parado[player_index].get_rect(midbottom = (1000, 600))

#Altera a escala dos personagens
#satiro_parado = pygame.transform.scale(satiro_parado, 420, 320)

#Define o titulo da janela
pygame.display.set_caption("Satyr - O Sátiro")

#Cria um relogio para controlar o FPS
relogio = pygame.time.Clock()

#################################################################################################################

#Loop
while jogo_ativo == 1:
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                acaotecla = 1
            elif evento.key == pygame.K_2:
                acaotecla = 2
            elif evento.key == pygame.K_ESCAPE:
                acaotecla == 3
                pygame.quit()
                exit()

    #Desenha o fundo na tela
    tela.blit(img_fundo, (0, 0))             
    tela.blit(img_sombra, (0, 0))
    tela.blit(img_janela, (0, 0))
    tela.blit(img_vela, (0, 0))
    tela.blit(img_arco, (0, 0))
    tela.blit(img_chao, (0,0))
    tela.blit(img_estatua, (0,0))
    tela.blit(img_placar, (20, 20))

    #Chama animação do personagens
    anima_player()
    anima_bot()

    #Chama Placares
    placar_satiro()
    placar_bot()

    #Encontro
    txt_evento = fonte_pixel.render('UM MINOTAURO APARECEU!', True, '#FFFFFF')
    txt_dialogo = fonte_pixel.render('(GRRRRRRRRR!!!)', True, '#FFFFFF')
    txt_acao1 = fonte_pixel.render('Escolha o que vai fazer', True, '#FFFFFF')
    txt_acao2 = fonte_pixel.render('VOCE NAO TEM CURA', True, '#FFFFFF')

    txt_acao = txt_acao1

    tela.blit(txt_evento, (450, 30))
    timer_txt = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_txt, 50)
    tela.blit(txt_dialogo, (500, 60))
    timer_txt = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_txt, 50)
    tela.blit(txt_acao, (460, 90))

    acaoescolhida = acaotecla
    if acaoescolhida == 1:
        rolagem()
        andar_player()
        life_bot -= rolagem_satiro
        if life_bot > 10:
            rolagem2()
            life_satiro -= rolagem_bot
        elif life_bot <= 10:
            if potion2 > 0:
                rolagem_bot = 0
                life_bot += 10
                potion2 -= 1
            else:
                pass
        
    elif acaoescolhida == 2:
        if potion1 > 0:
            potion1 -= 1
            life_satiro += 10
            acaotecla = 0
            if life_bot > 10:
                rolagem2()
                life_satiro -= rolagem_bot
            elif life_bot <= 10:
                if potion2 > 0:
                    rolagem_bot = 0
                    life_bot += 10
                    potion2 -= 1
                else:
                    if life_bot > 10:
                        rolagem2()
                        life_satiro -= rolagem_bot
                    elif life_bot <= 10:
                        if potion2 > 0:
                            life_bot += 10
                            potion2 -= 1
                    
        else:
            txt_acao = txt_acao2
            tela.blit(txt_acao, (460, 90))
            acaotecla = 0
            timer_txt = pygame.USEREVENT + 1
            pygame.time.set_timer(timer_txt, 50)
            txt_acao = txt_acao1
    #Atualiza a tela com o conteudo
    pygame.display.update()
    
    #Define a quantidade de frames por segundo
    relogio.tick(60)

#Encerra o jogo

tela.blit(img_fundo, (0, 0))
tela.blit(img_placar, (20, 20))
txt_evento = fonte_pixel.render('FIM DE JOGO!', True, '#FFFFFF')
txt_dialogo = fonte_pixel.render('PRESSIONE ESC PARA SAIR', True, '#FFFFFF')
tela.blit(txt_evento, (450, 30))
tela.blit(txt_dialogo, (300, 60))

#Atualiza a tela com o conteudo
pygame.display.update()
    
#Define a quantidade de frames por segundo
relogio.tick(60)