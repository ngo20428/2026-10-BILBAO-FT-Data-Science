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

        barcos_puestos = [
            # Eslora = 1 (4 barcos)
            [(0, 6)],
            [(2, 6)],
            [(4, 6)],
            [(6, 6)],

            # Eslora = 2 (3 barcos)
            [(4, 0), (4, 1)],
            [(6, 0), (6, 1)],
            [(8, 0), (9, 0)],

            # Eslora = 3 (2 barcos)
            [(2, 0), (2, 1), (2, 2)],
            [(1, 0), (1, 1), (1, 2)],

            # Eslora = 4 (1 barco)
            [(0, 0), (0, 1), (0, 2), (0, 3)]
        ]

        for itsasontzi in barcos_puestos:
            for fila, columna in itsasontzi:
                self.tablero[fila][columna] = barco


    
    def disparar(self, fila, columna):
        ''' Comprobamos que las coordenadas introducidas son válidas (es decir, que están dentro del tablero).'''
        if not (0 <= fila < filas and 0 <= columna < columnas):
            return "Error. Las coordenadas tienen que estar entre 0 y 9."
    
        # Comprobar si ya se había disparado en dicha coordenada
        if self.tablero[fila][columna] == fallo or self.tablero[fila][columna] == impacto:
            return "Ya has disparado ahí."
    
        # Si hemos dado a un barco:
        if self.tablero[fila][columna] == barco:
            self.tablero[fila][columna] = impacto
            self.barcos_restantes -= 1
            return "¡Le has dado!"
    
        # Si no, hemos dado a aguaa
        if self.tablero[fila][columna] == agua:
            self.tablero[fila][columna] = fallo
            return "Agua :("

    def registrar_disparo(self, fila, columna, resultado):
        if resultado == "impacto":
            self.tablero_disparos[fila][columna] = impacto
        else:
            self.tablero_disparos[fila][columna] = fallo

    def mostrar_tablero(self, tablero=None):
    # Si no se indica otro tablero, mostramos el propio if tablero is None: tablero = self.tablero
        pprint.pprint(tablero)
