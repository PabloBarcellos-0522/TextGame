import pygame
pygame.init()

def teclas(evento, altura, historico, entrada_usuario, offset):
    if evento.key == pygame.K_BACKSPACE:
        entrada_usuario = entrada_usuario[:-1]
    elif evento.key == pygame.K_UP:
        offset = max(0, offset - 70)
    elif evento.key == pygame.K_DOWN:
        offset = max(0, offset + 70)
    else:
        entrada_usuario += evento.unicode
    
    return offset, entrada_usuario
