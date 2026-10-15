# FUNCIONES

from variables import(
    filas,
    columnas,
    barcos_def,
    agua,
    barco,
    impacto,
    fallo
)

import pprint

def disparar(tablero, fila, columna):
    ''' Comprobamos que las coordenadas introducidas son válidas (es decir, que están dentro del tablero).'''
    if not (0 <= fila < tablero.filas and 0 <= columna < tablero.columnas):
        return "Error. Las coordenadas tienen que estar entre 0 y 9."

    '''Establecemos la coordenada como una casilla'''
    casilla = tablero.tablero[fila][columna]

    # Comprobar si ya se había disparado en dicha casilla
    if casilla == fallo or casilla == impacto:
        return "Ya has disparado ahí."

    # Comprobar si hemos dado a un barco
    if casilla == barco:
        tablero.tablero[fila][columna] = impacto
        tablero.barcos_restantes -= 1
        return "¡Le has dado!"

    # Si no, hemos dado a agua
    tablero.tablero[fila][columna] = agua
    return "Agua :("


def comprobar_mi_tablero(tablero):
    pprint.pprint(tablero)