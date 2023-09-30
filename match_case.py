#!/usr/local/bin/python3

from random import randint

def par_impar (sorteio):
    match sorteio:
        case 1 | 3 | 5:
            return "Impar"
        case 2 | 4 | 6:
            return "Par"
        case _:
            return "Fora da faixa até 6"

sorteio = randint(0,9)
resultado = par_impar(sorteio)
print(f"O numero sorteado é {sorteio} e o resultado é {resultado}")




