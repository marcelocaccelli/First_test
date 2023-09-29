#!/usr/local/bin/python3

import sys

print("Ola")
print("Nome do modulo",__name__)

script = sys.argv[0] # O argv é uma lista de argumentos sendo index 0 o nome do script python
print(script)

argumento_fornec = sys.argv[1] # O argv é uma lista de argumentos sendo index 1 o nome do dado digitado diretamente mo terminal python
print(argumento_fornec)


print("Fim")

