#importação e atribuições:
import sqlite3

conexao = sqlite3.connect('./Banco.db')
cursor = conexao.cursor()


#criação de tabela/instrução/comando sql:
def criarTabela():
    comando = '''
        CREATE TABLE IF NOT EXISTS PLAYER (
            ID INTEGER PRIMARY KEY,
            NOME VARCHAR(100), 
            GENERO BOOLEAN, 
            DATA TEXT, 
            CRIACAO DATETIME2(6))
'''
    cursor.execute(comando)

#inserir informações, forma 1:
def inserirInf(ID, NOME, GENERO, ATRIBUTOS, TIME):
    comando = "INSERT INTO PLAYER VALUES(?, ?, ?, ?, ?)"
    cursor.execute(comando, (ID, NOME, GENERO, ATRIBUTOS, TIME))
    conexao.commit()
    cursor.execute("SELECT ID FROM PLAYER WHERE CRIACAO = (SELECT MAX(CRIACAO) FROM PLAYER)")
    return cursor.fetchall()[0]

#inserir informações, forma 2:
# def inserirInf2(comando, registros):
#     for registro in registros:
#         print(comando, registro)
#         cursor.execute(comando, registro)
#         conexao.commit()
#         cursor.execute("SELECT ID FROM PLAYER WHERE CRIACAO = (SELECT MAX(CRIACAO) FROM PLAYER)")
#     return cursor.fetchall()[0]

#ler registros (TODOS):
def mostarRegistros():
    comando = 'select * from PLAYER'#<---NOME DA TABELA
    cursor.execute(comando)
    dados = cursor.fetchall()
    for linha in dados:
        print('ID: %d, Nome: %s, Gênero: %s , Lista: %s, Data_Criação: %s' % linha)

#ler registros (ESPECÍFICOS):
def ler_registros(ID):
    cursor.execute(f"SELECT DATA FROM PLAYER WHERE ID = {ID}")#<---- categoria do registro
    return cursor.fetchone()[0]
    # for linha in cursor.fetchall():
    #     #a = list(linha)[1]
    #     a = list(linha)
    #     print(f"\n\n{a}")

# def updateRegistros():
#     cursor.execute("UPDATE PLAYER SET TITULO = '123' WHERE ID = 2")#<---- id do registro
#     conexao.commit()

# #delete registros:
    # cursor.execute("DELETE FROM VIDEOS WHERE ID = 2")#<---- id do registro
    # conexao.commit()

# criarTabela()
# inserirInf('INSERT INTO PLAYER VALUES(?, ?)', [(1, 'Pablo Gênio')])
# mostarRegistros()











# import sqlite3
# import json

# # Conectar ao banco de dados
# conn = sqlite3.connect('example.db')
# c = conn.cursor()

# # Criar a tabela
# c.execute('''CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, data TEXT)''')

# # Lista a ser armazenada
# my_list = [1, 2, 3, 4, 5]

# # Serializar a lista em JSON
# my_list_json = json.dumps(my_list)

# # Inserir a lista serializada no banco de dados
# c.execute('''INSERT INTO my_table (data) VALUES (?)''', (my_list_json,))
# conn.commit()


# Recuperar a lista serializada do banco de dados
# c.execute('''SELECT data FROM my_table WHERE id = 1''')
# data = c.fetchone()[0]

# # Desserializar a lista
# my_list = json.loads(data)

# print(my_list)  # Output: [1, 2, 3, 4, 5]

# # Fechar a conexão
# conn.close()
