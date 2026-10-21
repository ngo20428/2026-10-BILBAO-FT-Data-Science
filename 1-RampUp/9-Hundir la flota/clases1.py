# CLASES

import random

from variables import *

class Tablero:

    def __init__(self, jugador):
        
        self.jugador = jugador
        
        # Tablero propio: en el que tenemos nuestros barcos + los disparos recibidos
        self.tablero_propio = [[agua for i in range(columnas)] for j in range(filas)]

        # Tablero "rival": en el que vamos registrando los disparos que vamos haciendo
        self.tablero_disparos = [[agua for i in range(columnas)] for j in range(filas)]

        # Llevamos registro de los barcos que siguen a flote
        self.barcos_restantes = sum(eslora * num 
                                    for eslora, num in barcos_dict.items())

        self.colocar_barcos()


    def colocar_barcos(self):
        """Coloca todos los barcos definidos en barcos_dict de forma aleatoria y aislada."""
        self.itsasontzis = [] # Es la lista de los barcos colocados
        
        # Es mejor colocar primero los barcos más grandes (4, 3, 2, 1) para evitar quedarnos sin espacio
        for eslora in sorted(barcos_dict.keys(), reverse=True):
            cantidad = barcos_dict[eslora]
            
            for i in range(cantidad):
                colocado = False
                
                while not colocado:
                    # Elegimos posición y orientación al azar
                    orientacion = random.choice(["H", "V"])
                    fila_aleatoria = random.randint(0, filas - 1)
                    col_aleatoria = random.randint(0, columnas - 1)

                    posiciones = []
                    
                    # Si la posición es válida, lo pintamos en el tablero
                    if self.es_posicion_valida(fila_aleatoria, col_aleatoria, eslora, orientacion):
                        if orientacion == "H":
                            for c in range(col_aleatoria, col_aleatoria + eslora):
                                self.tablero_propio[fila_aleatoria][c] = barco
                                posiciones.append((fila_aleatoria, c))

                        else: # Vertical
                            for r in range(fila_aleatoria, fila_aleatoria + eslora):
                                self.tablero_propio[r][col_aleatoria] = barco
                                posiciones.append((r, col_aleatoria))

                        self.itsasontzis.append(set(posiciones))
                        
                        colocado = True # Rompe el bucle while y pasa al siguiente barco
    

    def recibir_disparo(self, fila, columna):
        
        # Si había barco:
        if self.tablero_propio[fila][columna] == barco:
            self.tablero_propio[fila][columna] = impacto # cambiamos el ikurra por el de impacto
            self.barcos_restantes -=1

            # Ahora comprobamos si el barco ha sido hundido o solo tocado
            for barco_tocado in self.itsasontzis:
                if (fila, columna) in barco_tocado:
                    barco_tocado.remove((fila, columna)) # Quitamos la posición disparada

                    # El barco está hundido cuando ya no le quedan posiciones:
                    hundido = len(barco_tocado) == 0

                    return "impacto", hundido
                    # "impacto", True --> el barco está hundido
                    # "impacto", False --> el barco solo ha sido tocado
        
        else: # Si no había barco --> había agua
            self.tablero_propio[fila][columna] = fallo
            return "fallo", False # Ni tocado ni hundido --> agua


    def registrar_disparo(self, fila, columna, resultado):
        if resultado == "impacto":
            self.tablero_disparos[fila][columna] = impacto
        
        elif resultado == "fallo":
            self.tablero_disparos[fila][columna] = fallo

    def disparo_repe(self, fila, columna):
        return self.tablero_disparos[fila][columna] != agua