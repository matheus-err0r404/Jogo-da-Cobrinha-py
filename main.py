# CONFIGURAÇÕES INICIAIS
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha py")
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores
preto = (0, 0, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
verde = (0, 255, 0)

#parametros da cobrinha
tamanho_quadrado = 20
velocidade_jogo = 12

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0 ) * 20.0 
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, amarelo, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, azul, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Montserrat", 30)
    texto = fonte.render(f"Pontos: {pontuacao}", False, verde)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
     velocidade_x = 0
     velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
     velocidade_x = 0
     velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
     velocidade_x = tamanho_quadrado
     velocidade_y = 0
    elif tecla == pygame.K_LEFT:
     velocidade_x = -tamanho_quadrado
     velocidade_y = 0   
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

# DESENHAR OS OBJETOS DO JOGO NA TELA
       
# CRIAR UM LOOP INFINITO
    while not fim_jogo:
        tela .fill(preto) 
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo =True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
                
        #atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        x += velocidade_x
        y += velocidade_y
              
        # desenhar comida        
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # desenhar cobrinha

        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]

        #verifica cobra bate na propria cobra
    
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        desenhar_cobra(tamanho_quadrado, pixels)            

        desenhar_pontuacao(tamanho_cobra - 1)
    
        #ATUALIZAÇÃO DA TELA
        pygame.display.update()
        
        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(velocidade_jogo)

rodar_jogo()