# FUNCIONES

import random

from variables import(
    filas,
    columnas,
    barcos_def,
    agua,
    barco,
    impacto,
    fallo
)


def mostrar_tableros(jugador, maquina):
    print("\n=== TU TABLERO ===") jugador.mostrar_tablero()
    print("\n=== TUS DISPAROS CONTRA LA MÁQUINA ===") jugador.mostrar_tablero(jugador.tablero_disparos)

def pedir_coordenadas():
    while True: 
        try: 
            fila = int(input("Introduce la fila (0-9): ")) 
            columna = int(input("Introduce la columna (0-9): "))
            if 0 <= fila < filas and 0 <= columna < columnas: 
                return fila, columna
            else:
                print("Error: las coordenadas deben estar entre 0 y 9.")
        except ValueError: 
            print("Error: introduce números enteros porfi :)")


def disparo_jugador(jugador, rival, fila, columna):
    if jugador.tablero_disparos[fila][columna] in (impacto, fallo):  
        return "Ya has disparado ahí."

resultado = rival.recibir_disparo(fila, columna)
Registramos el resultado en el tablero de disparos
jugador.registrardisparorival(fila, columna, resultado)
if resultado == "impacto": print("¡Tocado! Has acertado.") elif resultado == "agua": print("Agua. Le toca a la máquina.")
return resultado
def disparo_maquina(maquina, jugador):
Escogemos una posición que todavía no hayamos atacado
while True: fila = random.randint(0, FILAS - 1) columna = random.randint(0, COLUMNAS - 1)
if jugador.tablero[fila][columna] not in (IMPACTO, FALLO): break
print(f"\nLa máquina dispara a la fila {fila}, columna {columna}.")
resultado = jugador.recibir_disparo(fila, columna)
Registramos también el resultado en el tablero de disparos
maquina.registrardisparorival(fila, columna, resultado)
if resultado == "impacto": print("¡La máquina te ha dado!") else: print("La máquina ha fallado.")
return resultado
