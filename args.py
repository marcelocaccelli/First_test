#!/usr/local/bin/python3

def tes_fun_normal_pos(arg1, arg2, arg3, arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print("==== posicional ^ ")


tes_fun_normal_pos(1, 2, 3, 4)
tes_fun_normal_pos(arg4=4, arg3=3, arg2=2, arg1=1)

# ===============================


def tes_fun_normal_nom(arg1=1, arg2=2, arg3=3, arg4=4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print("==== nomeada ^ ")


tes_fun_normal_nom(1, 2, 3, 4)
tes_fun_normal_nom(arg4=4, arg3=3, arg2=2, arg1=1)
tes_fun_normal_nom(arg4=4, arg3=3)
tes_fun_normal_nom(arg2=2, arg1=1)

# ===============================

def tes_fun_arg(arg1, *args):
    print(arg1)
    for items in args:
        print(items)
    print("==== usando args ^ ")

lista =[2,3,4]
tupla =(2,3,4)

tes_fun_arg(1,2,3,4)
tes_fun_arg(1,*lista)
tes_fun_arg(1,*tupla)
tes_fun_arg(1,*lista,"Se nao colocar param nomeado aqui fica, tudo que for posicional sera inserido na tupla interna a funcao")
tes_fun_arg(1,*tupla,"Se nao colocar param nomeado aqui fica, tudo que for posicional sera inserido na tupla interna a funcao")

# ===============================

def tes_fun_arg2(arg1=1, *args, arg4=4, arg5="Após o *args todo param deve ser nomeado"):
    print(arg1)
    for items in args:
        print(items)
    print(arg4)
    print(arg5)
    print("==== usando args2 ^ ")

lista2 =[2,3]
tupla2 =(2,3)

tes_fun_arg2(1,*lista2)
tes_fun_arg2(1,*lista2,arg4=4)
tes_fun_arg2(1,*lista2,arg4=4,arg5="Sempre nomeado apos *args")
# tes_fun_arg2(arg1=1,*lista2) # todos parametros antes de *args devem ser posicionais e depois devem ser nomeados.
print("término")
