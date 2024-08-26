import sys
import os
import time
from Dados.Jogador import *
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Janela import *


fade_img = pygame.Surface((largura, altura)).convert_alpha()
fade_img.fill((0, 0, 0))
fade = fade_img.get_rect()

img = pygame.image.load('Interface/Imagens/button.png')
button = pygame.transform.scale(img, (150, 50))
button_rect = button.get_rect()
button_rect2 = button.get_rect()
button_rect3 = button.get_rect()

button_rect.center = (largura / 2, altura / 2 - 70)
button_rect2.center = (largura / 2, altura / 2)
button_rect3.center = (largura / 2, altura / 2 + 70)



efeito_sonoro = pygame.mixer.Sound('Interface/Sons/deep-strange.mp3')
efeito_sonoro.set_volume(1)

botaoHover2 = pygame.mixer.Sound('Interface/Sons/mouse-click.mp3')
botaoHover = pygame.mixer.Sound('Interface/Sons/hover.mp3')



def TelaInicial():
    
    fade_alpha = 255
    logo_alpha = 0
    # logo = pygame.image.load('Interface/Server_img.jpg').convert_alpha()
    logo = pygame.image.load('Interface/Imagens/Logo.png').convert_alpha()
    logo = pygame.transform.scale(logo, (350, 350))
    logo_rect2 = logo.get_rect()
    logo_rect2.center = (largura / 2, altura / 2)


    logo.set_alpha(logo_alpha)
    janela.fill((0, 0, 0))
    janela.blit(fade_img, fade)
    janela.blit(logo, logo_rect2.topleft)
    pygame.display.flip()

    efeito_sonoro.play()
    while logo_alpha != 50:
        logo.set_alpha(logo_alpha)
        janela.blit(logo, logo_rect2)
        logo_alpha += 1
        pygame.display.update()
        time.sleep(0.03)
    time.sleep(3)
    
    a = (0,0)
    
    condicao = True
    while condicao:
        if fade_alpha > 0:
            fade_alpha -= 0.5
        else:
            condicao = False
            return botoes()
            # condicao = False

        fade_img.set_alpha(fade_alpha)
        janela.fill((0, 0, 0))  # Preenche a tela com preto antes de desenhar o fade

        # janela.blit(button, (largura / 2 - 75, altura / 2 - 125))
        # janela.blit(button, button_rect.topleft)
        # janela.blit(button, (largura / 2 - 75, altura / 2 + 75))
        janela.blit(button, button_rect.topleft)
        janela.blit(button, button_rect2.topleft)
        janela.blit(button, button_rect3.topleft)

        janela.blit(fade_img, fade)
        # pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    janela.fill((255, 255, 255))
                    
            # elif evento.type == pygame.MOUSEBUTTONDOWN:
            #     if button_rect.collidepoint(evento.pos):
            #         print("Botão 1 clicado!")
            #         condicao = False
            #     elif button_rect2.collidepoint(evento.pos):
            #         print("Botão 2 clicado!")
            #         condicao = False
            #     elif button_rect3.collidepoint(evento.pos):
            #         print("Botão 3 clicado!")
            #         condicao = False

        # mouse_pos = pygame.mouse.get_pos()
        # for numero in [button_rect, button_rect2, button_rect3]:
        #     if numero.collidepoint(mouse_pos) and not numero.collidepoint(a):
        #         botaoHover.play()

        pygame.display.flip()


def botoes():
    a = (0,0)
    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Detecta clique no botão
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(evento.pos):
                    print("Botão 1 clicado!")
                    running = False
                    Dados_jogador = SlotSave(1)
                    return Dados_jogador
                elif button_rect2.collidepoint(evento.pos):
                    print("Botão 2 clicado!")
                    Dados_jogador = SlotSave(2)
                    running = False
                    return Dados_jogador
                elif button_rect3.collidepoint(evento.pos):
                    print("Botão 3 clicado!")
                    Dados_jogador = SlotSave(3)
                    running = False
                    return Dados_jogador
                

        # Detecta se o mouse está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        for button in [button_rect, button_rect2, button_rect3]:
            # if button.collidepoint(mouse_pos) != button.collidepoint(a):
            #     botaoHover.play()
            if button.collidepoint(mouse_pos) and not button.collidepoint(a):
                botaoHover.play()
        a = mouse_pos

        pygame.display.flip()

