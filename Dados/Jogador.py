from BancoDeDados import *
import datetime
import json

class Player:
    def __init__(self, nome, genero):
        criarTabela()
        self.nome = nome
        if genero == 1:
            self.genero = True
        elif genero == 0: 
            self.genero = False
        self.ID = int(''.join(map(str, 
                inserirInf(None, nome, self.genero, None, datetime.datetime.now()
        )))) 
        self.level = 0
        self.ultimoDialogo = ""
        self.money = 0
        self.roupas = False
        self.key2 = False
        self.macaneta = False
        self.salvar()

    def salvar(self):
        self.atributos = [getattr(self, atributo) for atributo in dir(self) 
                    if not callable(getattr(self, atributo))and not atributo.startswith("__")]

        self.atributos_json = json.dumps(self.atributos)
        comando = f"UPDATE PLAYER SET DATA = '{self.atributos_json}' WHERE ID = {self.ID}"
        cursor.execute(comando)
        conexao.commit()
    

class SlotSave:
    def __init__(self, ID):
        self.nome = "Undefined"
        self.genero = False
        self.ID = ID
        self.level = 0
        self.ultimoDialogo = ""
        self.money = 0
        self.roupas = False
        self.key2 = False
        self.macaneta = False
        self.montarPlayer()

    def salvar(self):
        self.atributos = [getattr(self, atributo) for atributo in dir(self) 
                    if not callable(getattr(self, atributo))and not atributo.startswith("__")]
        print(self.atributos)

        self.atributos_json = json.dumps(self.atributos)
        comando = f"UPDATE PLAYER SET DATA = '{self.atributos_json}' WHERE ID = {self.ID}"
        cursor.execute(comando)
        conexao.commit()

    def montarPlayer(self):
        atributos = [atributo for atributo in dir(self) 
                        if not callable(getattr(self, atributo)) and not atributo.startswith("__")]
        
        dados = ler_registros(self.ID)
        index = 0
        for atributo in atributos:
            setattr(self, atributo, json.loads(dados)[index])
            index += 1
        
# save1 = Player("Maria", 0)
save1 = SlotSave(6)
mostarRegistros()