#!/usr/local/bin/python3

# Criando dicionario no modo convencional


dicionario = {}

for chaves in range(1, 10):
    dicionario.update({chaves: " "})

print(dicionario)


# Criando dicionario utilizando comprehension sem condicional
dic_compreh = {chaves_c: "*" for chaves_c in range(1, 10)}
print(dic_compreh)

# lendo os valores após a criação
for chvs, valores in dic_compreh.items():
    print(f"A chave é {chvs} e o valor é {valores}")

# Criando dicionario utilizando comprehension com condicional

dic_compreh2 = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dic_compreh2)

# lendo os valores após a criação
for numero, dobro in dic_compreh2.items():
    print(f'{numero} x 2 = {dobro}')
