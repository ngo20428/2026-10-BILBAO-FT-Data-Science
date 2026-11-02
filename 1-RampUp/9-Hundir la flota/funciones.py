# FUNCIONES

import random

from variables import *
from clases import *


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))


def coordenadas():

    while True:
        fila = input("Introduce la fila (0-9): ")
        columna = input("Introduce la columna (0-9): ")

        if fila.isdigit() and columna.isdigit():
            fila = int(fila)
            columna = int(columna)

            if (0 <= fila < filas and 0 <= columna < columnas):
                return fila, columna
                break
            else:
                print("Las coordenadas tienen que estar entre 0 y 9, que si no disparas fuera, capitán!")
                continue

        else:
            print("Mete solo números del 0 al 9, porfi :)")


def disparo_maquina():
    fila = random.randint(0, filas -1)
    columna = random.randint(0, columnas -1)
    return fila, columna
    