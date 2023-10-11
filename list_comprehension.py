#!/usr/local/bin/python3


# Modo normal para criar uma lista
lista = []
for item in range(0, 10):
    if item % 2 == 0:
        lista.append(item * 2)

print(lista)


lista_comprehension = [item * 2 for item in range(0, 10) if item % 2 == 0]

print(lista_comprehension)
