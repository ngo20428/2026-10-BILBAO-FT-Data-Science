# MAIN

from clases import Tablero
from funciones1 import pedir_coordenadas, realizar_disparo, turno_maquina


def main():
    print("=" * 40)
    print("       ¡BIENVENIDO A HUNDIR LA FLOTA!")
    print("=" * 40)
    print("Destruye todos los barcos de la máquina para ganar.")
    print("Introduce las coordenadas de fila y columna entre 0 y 9.")
    print("Si aciertas, vuelves a disparar.")
    print("Símbolos: B = barco, X = impacto, O = agua.")
    print("~ = casilla sin explorar.\n")

    # Crear los tableros una sola vez
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")

    # Bucle principal del juego
    while True:

        print("\n" + "=" * 40)
        print("TU TURNO")
        print("=" * 40)

        # Mostrar el tablero propio y los disparos realizados
        jugador.mostrar_tablero()
        jugador.mostrar_disparos()
        print(f"Tus barcos restantes: {jugador.barcos_restantes}")
        print(f"Barcos restantes de la máquina: {maquina.barcos_restantes}")

        fila, columna = pedir_coordenadas(maquina)

        resultado = realizar_disparo(
            jugador, maquina, fila, columna
        )

        # Si acierta, vuelve a disparar
        if resultado == "X":

            if maquina.barcos_restantes == 0:
                print("\n¡ENHORABUENA! Has hundido todos los barcos.")
                print("¡HAS GANADO!")
                break

            continue

        # Si falla, es el turno de la máquina
        print("\nTurno de la máquina...")

        turno_maquina(maquina, jugador)

        # Comprobar si la máquina ha ganado
        if jugador.barcos_restantes == 0:
            print("\nLa máquina ha hundido todos tus barcos.")
            print("¡HA GANADO LA MÁQUINA!")
            break

main()