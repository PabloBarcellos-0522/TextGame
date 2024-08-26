from Janela import *
import pygame
pygame.init()

historico = [["Você acorda num quarto, no seu lado tem um criado-mudo que em cima tem uma foto de uma menina ao lado de uma homem.",[255, 255, 255]]]
fonte = pygame.font.Font(None, 25) # tamanho do texto
cor_texto = (255, 255, 255) # cor do texto

# Função para exibir texto na janela
def exibir_texto(texto, y):
    superficie_texto = fonte.render(texto[0], True, obterCor(texto[1]))
    janela.blit(superficie_texto, (10, y))

def obterCor(object):
    r = object[0]
    g = object[1]
    b = object[2]
    cor_texto = (r, g, b)
    return cor_texto