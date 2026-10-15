# FUNCIONES

import random

from variables import filas, columnas, agua, impacto, fallo

def pedir_coordenadas(tablero_rival):

    while True:
        try:
            fila = int(input("Introduce la fila (0-9): "))
            columna = int(input("Introduce la columna (0-9): "))

            if not (0 <= fila < filas and 0 <= columna < columnas):
                print("Coordenadas fuera del tablero. Inténtalo de nuevo.")
                continue

            if tablero_rival.tablero_disparos[fila][columna] != agua:
                print("Ya has disparado en esa posición. Prueba otra.")
                continue

            return fila, columna

        except ValueError:
            print("Debes introducir números enteros.")


def realizar_disparo(jugador, rival, fila, columna):

    resultado = rival.disparar(fila, columna)

    # Registrar el resultado en el tablero de disparos
    jugador.tablero_disparos[fila][columna] = resultado

    if resultado == impacto:
        print("¡Tocado! Has acertado.")
    elif resultado == fallo:
        print("Agua. No había ningún barco.")
    else:
        print("Esa posición ya había recibido un disparo.")

    return resultado


def turno_maquina(maquina, jugador):

    while True:
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)

        # La máquina no debe repetir disparos
        if jugador.tablero[fila][columna] in (impacto, fallo):
            continue

        print(f"\nLa máquina dispara a la fila {fila}, columna {columna}.")

        resultado = realizar_disparo(
            maquina, jugador, fila, columna
        )

        if resultado == impacto:
            # Si acierta, vuelve a disparar
            if jugador.barcos_restantes == 0:
                return
            continue

        # Si falla, termina su turno
        break