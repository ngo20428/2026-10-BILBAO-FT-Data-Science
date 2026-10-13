# CLASES

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

        barcos_puestos = [
            # Eslora = 1 (4 barcos)
            [(0, 6)],
            [(2, 6)],
            [(4, 6)],
            [(6, 6)],

            # Eslora = 2 (3 barcos)
            [(4, 0), (4, 1)],
            [(6, 0), (6, 1)],
            [(8, 3), (8, 4)],

            # Eslora = 3 (2 barcos)
            [(2, 0), (2, 1), (2, 2)],
            [(9, 5), (9, 6), (9, 7)],

            # Eslora = 4 (1 barco)
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        ]

        for itsasontzi in barcos_puestos:
            for fila, columna in itsasontzi:
                self.tablero[fila][columna] = barco

    