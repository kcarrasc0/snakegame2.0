#configurações inciais
import pygame
import random
import tkinter as tk
import random
from perguntas import JogoPerguntaUnica

pygame.init()
pygame.display.set_caption('Jogo de português')
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
direcao_atual = "parado"

# Matriz de perguntas e respostas
#PARA MUDAR AS PERGUNTAS É AQUI!!
perguntas_respostas = [
    #["pergunta", "resposta"]
    ["Qual é a capital do Brasil?", "Brasília"],
    ["Qual é a cor do céu em um dia ensolarado?", "Azul"],
    ["Quanto é 2 + 2?", "4"]
]

# cores
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobra
tamanho_quadrado = 20
velocidade_atualizacao = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura-tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura-tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('Comic sans', 35)
    texto = fonte.render(f'Pontos: {pontuacao}', True, vermelho)
    tela.blit(texto, [1, 1])
    
def selecionar_velocidade(tecla):
    global direcao_atual, velocidade_x, velocidade_y  # Definindo a variável como global

    if tecla == pygame.K_DOWN and direcao_atual != "cima":
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        direcao_atual = "baixo"
    elif tecla == pygame.K_UP and direcao_atual != "baixo":
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        direcao_atual = "cima"
    elif tecla == pygame.K_RIGHT and direcao_atual != "esquerda":
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
        direcao_atual = "direita"
    elif tecla == pygame.K_LEFT and direcao_atual != "direita":
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
        direcao_atual = "esquerda"

    return velocidade_x, velocidade_y, direcao_atual

def perguntas():
    global perguntas
    janela = tk.Tk()
    pergunta = tk.Entry(janela)
    pergunta.pack()
    return 

def jogar():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0
    
    
    

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preto)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y, direcao_atual = selecionar_velocidade(evento.key)

        # desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar posicao cobra
        if x < 0 or x >= largura or y <0 or y >= altura:
            fim_jogo = True
        x += velocidade_x
        y += velocidade_y

        # desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        #bateu no corpo
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)
        # desenhar pontos
        desenhar_pontuacao(tamanho_cobra - 1)
        # atualizar tela
        pygame.display.update()

        

        #cria comida
        if x == comida_x and y == comida_y:
            jogo = JogoPerguntaUnica(perguntas_respostas)
            jogo.iniciar()
            if jogo.fim_jogo == True:
                fim_jogo = True
            tamanho_cobra +=1
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_atualizacao)
    pass

# criar um loop infinito
jogar()

