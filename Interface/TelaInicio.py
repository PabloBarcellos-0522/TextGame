import sys
import os
import time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Janela import *

def TelaInicial():
    fade_alpha = 255
    fade_img = pygame.Surface((largura, altura)).convert_alpha()
    fade_img.fill((255, 255, 255))
    fade = fade_img.get_rect()

    img = pygame.image.load('Interface/button.png')
    button = pygame.transform.scale(img, (150, 50))
    button_rect = button.get_rect()
    button_rect.center = (largura / 2, altura / 2)

    efeito_sonoro = pygame.mixer.Sound('Interface/Sons/deep-strange.mp3')


    janela.blit(fade_img, fade)
    pygame.display.flip()
    efeito_sonoro.play()
    time.sleep(5)
    condicao = True
    while condicao:
        if fade_alpha > 0:
            fade_alpha -= 0.5

        fade_img.set_alpha(fade_alpha)
        janela.fill((0, 0, 0))  # Preenche a tela com preto antes de desenhar o fade
        # janela.blit(button, [largura/2 -50, altura/2 -25])
        janela.blit(button, button_rect.topleft)
        janela.blit(fade_img, fade)
        # pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    janela.fill((255, 255, 255))
                    # condicao = False

        pygame.display.flip()
