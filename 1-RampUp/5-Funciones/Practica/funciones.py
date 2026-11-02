import math

def cambialistas(lista, comando, elemento):
    if comando == "add":
        lista.append(elemento)

    elif comando == "remove":
        lista.remove(elemento)

    return lista

def frasear(*palabras):
    lista = []
    for palabra in palabras:
        lista.append(palabra)
    
    return " ".join(lista)

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def area_cuadrados(lado):
    area = lado * lado
    return area

def area_triangulos(base, altura):
    area = base * altura / 2
    return area

def area_circulos(radio):
    area = math.pi * radio**2
    return area