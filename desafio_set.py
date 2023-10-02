#!/usr/local/bin/python3

PALAVRAS_PROIBIDAS = {"futebol", "politica", "religiao"}
frases = ["A Paula gosta de politica e religiao"," O Marcelo gosta de futebol","O Miguel gosta de ir na praia"]

for texto in frases:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao: # Neste caso um conjunto vazio retorna False, aqui ele verifica se ele não esta vazio gerando True.
        print("Foi encontrado as seguintes palavras proibidas", intersecao)
    else: # Caso o conjunto intersecao esteja vazio o else entra em ação.
        print("Frase(s) liberadas:",texto)









#for texto in textos:
#    for palavra in texto.lower().split:
#        conjunto.append(palavra)