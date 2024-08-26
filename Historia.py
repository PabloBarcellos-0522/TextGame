from Texto import *
# from Dados.Jogador import *
# def Historia(entrada_usuario):
#     if entrada_usuario == "abrir porta":
#         historico.append("Você abriu a porta e encontrou um corredor iluminado.")
#     elif entrada_usuario == "procurar ao redor":
#         historico.append("Você encontrou uma chave no chão.")
#     else:
#         historico.append("Escolha inválida.")




# b.update({'ir para o banheiro': "nova frase"})

level1 = {
    'ir para o banheiro':
    [('Você se levanta e vai para o banheiro lavar o rosto, e percebe que a menina da foto é você.', [255, 255, 255]),
        True],
    'ir para a cozinha':
    [('Você chega na cozinha e vê o homem da foto cozinhando e ele diz: “Bom dia Sofia!, que tal você levar o seu rosto no banheiro enquanto eu faço o café da manhã?”',[255, 255, 255]),
        True],
}

level2 = {
    'Oeste':
    [('Você se depara com um rio cheio de peixes.',[255, 255, 255]),
        True],
    'Norte':
    [('Você chegou em uma montanha gélida.',[255, 255, 255]),
        True],
    'Sul':
    [('Você encontra uma caverna muito escura.',[255, 255, 255]),
        True],
    'Leste':
    [('Você encontra uma vila.',[255, 255, 255]),
        True],
    
}

level3 = {}


leveis = {1: level1, 2: level2, 3: level3}

def verificarInput(level, entrada_usuario, offset):
    modificarFrases(entrada_usuario, level)
    for key in level.keys():
        if entrada_usuario == key and level.get(key)[1]:
            if historico[-2] == ["Escolha inválida.",[255, 255, 255]]:
                historico.pop(-2)
                historico.pop(-2)
                offset -= 50
            historico.append(level.get(key)[0])
            return offset
    if historico[-2] != ["Escolha inválida.",[255, 255, 255]]:
        historico.append(["Escolha inválida.",[255, 255, 255]])
    else:
        if entrada_usuario != '':
            historico.pop(-2)
            historico.pop(-2)
            offset -= 50
            verificarInput(level, entrada_usuario, offset)
        else:
            historico.pop(-1)
            historico.pop(-1)
            offset -= 50
            verificarInput(level, entrada_usuario, offset)
    return offset

#frase que muda frase que muda nome que muda nome
index = {
    'ir para o banheiro':
    ['ir para a cozinha', [('Nova Frase',[255, 255, 255]),
        True]]
        
}

def modificarFrases(entrada_usuario, level):
    for frase in index.keys():
        if entrada_usuario == frase:
            level.update({index.get(frase)[0]: index.get(frase)[1]})