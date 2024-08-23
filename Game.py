import pygame
import tkinter as tk
import sys
from Texto import *
from Janela import *
from Historia import *
from Teclas import *

# comando para criar executavel pelo terminal: pyinstaller -F -W Game.py
# comando melhor: pyinstaller --noconsole --name="Executador de Projetos" --icon="NomeDoIcone.ico" --add-data="NomeDoIcone.ico;." --onefile main.py 

# Inicializa o pygame
pygame.init()

# Cor de fundo
cor_fundo = (0, 0, 0) 

# Função principal
def main():
    entrada_usuario = ""
    y = 10
    offset = 0

   # Programa
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if entrada_usuario == 'sair':
                        pygame.quit()
                        sys.exit()
                    historico.append([entrada_usuario,[255,255,0]])
                    offset = len(historico) * 25
                    offset = verificarInput(level1, entrada_usuario, offset)
                    entrada_usuario = ""
                else:
                    offset, entrada_usuario = teclas(evento, altura, historico, entrada_usuario, offset)
            elif evento.type == pygame.MOUSEWHEEL:
                offset = offset - evento.y * 30

        janela.fill(cor_fundo)

        y = altura - 70 - offset
        for linha in historico:
            exibir_texto(linha, y)
            y += 25

        # exibir_texto([(""),[0, 255, 0]], y)
        exibir_texto([">>> " + entrada_usuario,[0, 255, 0]], y)
        pygame.display.flip()

if __name__ == "__main__":
    main()