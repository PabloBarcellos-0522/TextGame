import pygame
import tkinter as tk
import sys
from Texto import *
from Janela import *
from Historia import *
from Teclas import *

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
                    historico.append(entrada_usuario)
                    # offset = min(len(historico) * altura + 50 - altura + 60, offset + 0)
                    offset = len(historico) * 25
                    # janelinha = tk.Tk()
                    # janelinha.title("Jogo de Texto")
                    # janelinha.mainloop()
                    # Historia(entrada_usuario)
                    verificarInput(level1, entrada_usuario)
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

        exibir_texto(">>> " + entrada_usuario, y)
        pygame.display.flip()

if __name__ == "__main__":
    main()