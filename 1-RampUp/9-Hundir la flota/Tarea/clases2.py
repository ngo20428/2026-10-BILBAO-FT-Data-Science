# CLASES

import pprint

from variables import(
    filas,
    columnas,
    barcos_def,
    agua,
    barco,
    impacto,
    fallo
)

class Tablero:

    def __init__(self, jugador):
        
        self.jugador = jugador
        
        # Tablero propio: en el que tenemos nuestros barcos + los disparos recibidos
        self.tablero = [[agua for i in range(columnas)] for j in range(filas)]

        # Tablero "rival": en el que vamos registrando los disparos que vamos haciendo
        self.tablero_disparos = [[agua for i in range(columnas)] for j in range(filas)]

        # Llevamos registro de los barcos que siguen a flote
        self.barcos_restantes = sum(eslora * num 
                                    for eslora, num in barcos_def.items())

        self.colocar_barcos()

    def colocar_barcos(self):

        # Posiciones fijas para la primera versión
        barcos_puestos = [
            # 4 barcos de eslora 1
            [(0, 6)],
            [(2, 6)],
            [(4, 6)],
            [(6, 6)],

            # 3 barcos de eslora 2
            [(4, 0), (4, 1)],
            [(6, 0), (6, 1)],
            [(8, 0), (9, 0)],

            # 2 barcos de eslora 3
            [(2, 0), (2, 1), (2, 2)],
            [(1, 0), (1, 1), (1, 2)],

            # 1 barco de eslora 4
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        ]

        for posiciones in barcos_puestos:
            for fila, columna in posiciones:
                self.tablero[fila][columna] = barco

    def disparar(self, fila, columna):

        # Comprobar qué hay en la posición elegida
        casilla = self.tablero[fila][columna]

        # Comprobar si ya se había disparado en dicha coordenada
        if casilla == fallo or casilla == impacto:
            return "Ya has disparado ahí."

        elif casilla == barco:
            self.tablero[fila][columna] = impacto
            self.barcos_restantes -= 1
            return impacto

        elif casilla == agua:
            self.tablero[fila][columna] = fallo
            return fallo


    def mostrar_tablero(self, ocultar_barcos=False):

        print(f"\nTablero de {self.jugador}")

        for i, fila in enumerate(self.tablero):
            if ocultar_barcos:
                # No mostrar los barcos que siguen intactos
                fila_visible = [
                    agua if casilla == barco else casilla
                    for casilla in fila
                ]
            else:
                fila_visible = fila

            print("  ".join(fila_visible))

    def mostrar_disparos(self):

        print(f"\nDisparos de {self.jugador}")
        pprint.pprint(self.tablero_disparos)