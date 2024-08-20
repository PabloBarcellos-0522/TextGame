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
    'abrir porta': ['Você abriu a porta e encontrou um corredor iluminado.', getKey1 and getKey2],
    "procurar ao redor": ["Você encontrou uma chave no chão.", getKey1 and getKey2]
}

def verificarInput(level, entrada_usuario):
    for key in level.keys():
        if entrada_usuario == key and level.get(key)[1]:
            # print(a, entrada_usuario, sala.get(a)[1])
            historico.append(level.get(key)[0])
            return 1
    historico.append("Escolha inválida.")
# verificarInput(level1, "abrir porta")

