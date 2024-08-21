#importação e atribuições:
import sqlite3
conexao = sqlite3.connect('./Testes/Banco.db')
cursor = conexao.cursor()

#criação de tabela/instrução/comando sql:
def criarTabela():
    comando = "CREATE TABLE PLAYER (ID INTEGER PRIMARY KEY, NOME VARCHAR(100))"
    cursor.execute(comando)

#inserir informações, forma 1:
    # cursor.execute("INSERT INTO VIDEOS VALUES(1, 'Banco de Dados SQlite', 'Banco de Dados')")
    # conexao.commit()

#inserir informações, forma 2:
def inserirInf(comando, registros):
    # comando = 'INSERT INTO PLAYER VALUES(?, ?)'
    # registros = [(2, 'Zezinho gostozo')]#<---- escreva todos os registros separados por virgula
    for registro in registros:
        print(registro[1])
        cursor.execute(comando, registro)
        conexao.commit()

#ler registros (TODOS):
def mostarRegistros():
    comando = 'select * from PLAYER'#<---NOME DA TABELA
    cursor.execute(comando)
    dados = cursor.fetchall()
    for linha in dados:
        print(dados)
        print('ID: %d, Nome: %s\n' % linha)

#ler registros (ESPECÍFICOS):
    # def ler_registros():
    #   cursor.execute("SELECT * FROM VIDEOS WHERE CATEGORIA = 'senha'")#<---- categoria do registro
    #   for linha in cursor.fetchall():
    #     #a = list(linha)[1]
    #     a = list(linha)
    #     print(f"\n\n{a}")
    # ler_registros()

#update registros:
    # cursor.execute("UPDATE VIDEOS SET TITULO = '123' WHERE ID = 2")#<---- id do registro
    # conexao.commit()

# #delete registros:
    # cursor.execute("DELETE FROM VIDEOS WHERE ID = 2")#<---- id do registro
    # conexao.commit()

criarTabela()
inserirInf('INSERT INTO PLAYER VALUES(?, ?)', [(1, 'Pablo Gênio')])
mostarRegistros()