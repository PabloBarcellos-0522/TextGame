from BancoDeDados import *

class Player:
    def __init__(self, nome, genero):
        criarTabela()
        self.ID = id
        self.nome = nome
        if genero == 'M':
            self.genero = True
        elif genero == 'F': 
            self.genero = False
        self.level = 0
        self.ultimoDialogo = ""
        self.money = 0
        self.roupas = False
        self.key2 = False
        self.macaneta = False

    def atualizarUltimoDialogo(self):

        self.ultimoDialogo = ""
        
save1 = Player("Maria", "F")

save1.nome = Player("Matheus", "F")