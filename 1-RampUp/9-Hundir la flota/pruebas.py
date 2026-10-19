# MAIN

from variables import *
from clases import *
from funciones1 import *

def main():

    print("----- HUNDIR LA FLOTA -----")
    print()
    print("Tu objetivo es hundir todos los barcos de la máquina antes de que ella derribe los tuyos :)")
    print("Introduce las coordenadas donde quieres disparar: una fila y una columna del 0-9")
    print("Si aciertas, vuelves a disparar.")
    print("Si fallas, le toca a la máquina.")
    print()
    print("Leyenda de los tableros:")
    print("X = impacto | O = fallo | B = barco | ~ = casilla sin disparar")

    # Creamos los tableros
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")


    # Se juega hasta que a alguno de los dos no le queden barcos
    while jugador.barcos_restantes > 0 and maquina.barcos_restantes > 0:

        # Bucle para el turno del jugador:
        while True:
            print("Te toca :)")
            print()
            print("Tu tablero:")
            mostrar_tablero(jugador.tablero_propio)
            print(f'Tus barcos restantes: {jugador.barcos_restantes}')
            print()
            print("Tus disparos a la máquina")
            mostrar_tablero(jugador.tablero_disparos)
            print(f'Barcos restantes de la máquina: {maquina.barcos_restantes}')

            print("¿Dónde atacamos, capitán?")
            fila, columna = coordenadas()

            # Comprobamos si ya ha disparado ahí
            if jugador.disparo_repe(fila, columna):
                print("¡Ya habías disparado ahí! Prueba otras coordenadas :)")
                continue

            resultado, hundido = maquina.recibir_disparo(fila, columna)
            jugador.registrar_disparo(fila, columna, resultado)

            if resultado == "impacto":

                if hundido:
                    print("¡Tocado y hundido! :)")

                else:
                    print("¡Le has dado! Buena puntería, capitán ;)")

                if maquina.barcos_restantes == 0:
                    break
                else:
                    continue

            else:
                print("¡Agua! :( Ahora le toca a la máquina.")
                break

        # Bucle para el turno de la máquina:
        while True:
            print("Turno de la máquina")

            while True:
                fila, columna = disparo_maquina()

                if not maquina.disparo_repe(fila, columna):
                    break

            resultado, hundido = jugador.recibir_disparo(fila, columna)
            maquina.registrar_disparo(fila, columna, resultado)

            if resultado == "impacto":

                if hundido:
                    print("¡Tocado y hundido! :C")

                else:
                    print("La máquina le ha dado! :(")

                if jugador.barcos_restantes == 0:
                    break
                else:
                    continue

            else:
                print("Ha disparado al agua. ¡Te toca atacar!")
                break

    # Fin de la partida
    print("\n --- FIN DE LA PARTIDA ----")

    if maquina.barcos_restantes == 0:
        print("¡Enhorabuena! ¡Has ganado! :)")

    else:
        print("La máquina ha ganado. ¡Otra vez será! :)")


main()