from Texto import *

def Historia(entrada_usuario):
    if entrada_usuario == "abrir porta":
        historico.append("Você abriu a porta e encontrou um corredor iluminado.")
    elif entrada_usuario == "procurar ao redor":
        historico.append("Você encontrou uma chave no chão.")
    else:
        historico.append("Escolha inválida.") 

getKey1 = True
getKey2 = True
level1 = {
    'abrir porta': 
    [('Você abriu a porta e encontrou um corredor iluminado.', [255, 255, 255]),
        getKey1 and getKey2],
    "procurar ao redor": 
    [("Você encontrou uma chave no chão.",[255, 255, 255]),
        getKey1 and getKey2]
}

level2 = {
    'Oeste':
    [('Você se depara com um rio cheio de peixes.',[255, 255, 255]),
        getKey1 and getKey2],
        'Norte':
    [('Você chegou em uma montanha gélida.',[255, 255, 255]),
        getKey1 and getKey2],
        'Sul':
    [('Você encontra uma caverna muito escura.',[255, 255, 255]),
        getKey1 and getKey2],
        'Leste':
    [('Você encontra uma vila.',[255, 255, 255]),
        getKey1 and getKey2],
    
}

def verificarInput(level, entrada_usuario, offset):
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