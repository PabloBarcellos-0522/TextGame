import tkinter as tk

# janelinha = tk.Tk()
# janelinha.title("Jogo de Texto")
# janelinha.mainloop()

def processar_escolha():
    escolha = entrada.get()
    if escolha == "abrir porta":
        resultado.config(text="Você abriu a porta e encontrou um corredor iluminado.")
    elif escolha == "procurar ao redor":
        resultado.config(text="Você encontrou uma chave no chão.")
    else:
        resultado.config(text="Escolha inválida.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Jogo de Texto")

# Widgets
texto = tk.Label(janela, text="Você está em uma sala escura. Há uma porta à sua frente.")
texto.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Enviar", command=processar_escolha)
botao.pack()

resultado = tk.Label(janela, text="")
resultado.pack()

# Inicia o loop principal da interface gráfica
janela.mainloop()