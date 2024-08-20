from Janela import *
import pygame
pygame.init()

historico = ["Você está em uma sala escura. Há uma porta à sua frente."]
fonte = pygame.font.Font(None, 25) # tamanho do texto
cor_texto = (255, 255, 255) # cor do texto

# Função para exibir texto na janela
def exibir_texto(texto, y):
    superficie_texto = fonte.render(texto, True, cor_texto)
    janela.blit(superficie_texto, (10, y))