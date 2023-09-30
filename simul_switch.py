#!/usr/local/bin/python3

def qualDia(dia):
    dias = {"segunda": "dia util", "terça": "dia util", "quarta": "dia util", 
            "quinta": "dia util", "sexta": "dia util", "sabado": "fim de semana",
            "domingo": "fim de semana"}
    return dias.get(dia)

tupla = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")

for varredura in tupla:
    print(f"O dia: {varredura} é {qualDia(varredura)}")