#!/usr/local/bin/python3

PALAVRAS_PROIBIDAS = ("futebol", "politica", "religiao")
textos = ["A Paula gosta de politica e religiao"," O Marcelo gosta de futebol","O Miguel gosta de ir na praia"]
encontrou = []

for texto in textos:
    flag = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            flag = True
            print("Encontrou pelo menos uma palavra proibida", palavra)
            break
    if flag == False:
        print(texto)