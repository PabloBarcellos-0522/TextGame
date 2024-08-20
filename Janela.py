import pygame
pygame.init()

# Configurações da janela
janela = pygame.display.set_mode() # criar janela
pygame.display.toggle_fullscreen() # tamnho da janela
pygame.display.set_caption('joguinho foda') # nome da janela
largura, altura = janela.get_size()