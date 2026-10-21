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

        self.itsasontzis = [] # Es la lista de los barcos colocados

        for eslora, cantidad in barcos_dict.items():
            # Colocamos todos los barcos de cada eslora
            for i in range(cantidad):
                colocado = False # Por defecto no están colocados
                while not colocado:
                    # Elegimos la posición y orientación aleatoriamente
                    fila = random.randint(0, filas - 1)
                    columna = random.randint(0, columnas -1)
                    orientacion = random.choice(["H", "V"])

                    posiciones = [] # Lo que va a ocupar el barco

                    for long in range(eslora):
                        '''Calculamos las casillas que ocupa el barco.
                        Si la orientación es horizontal --> el número de fila se mantiene igual pero vamos sumando el índice
                                                        de posición a la columna.
                                                        Adb. si la col. random es 2 y el barco es eslora 3: 2+0, 2+1, 2+2
                        En cambio, si la orientación es vertical --> el nº de fila es el que cambia, y la col se mantiene ='''
                        if orientacion == "H":
                            posiciones.append((fila, columna + long))
                        else:
                            posiciones.append((fila + long, columna))

                    # Comprobamos si todas las posiciones del barco están dentro del tablero:
                    cabe = all(0 <= ilara < filas and 0 <= zutabe < columnas
                               for ilara, zutabe in posiciones)


                    # Comprobamos ahora si el tablero está libre.
                    # Consideramos que el tablero está libre para posicionar el barco si:
                        # 1. El barco cabe
                        # 2. Hay agua en dicha posición, es decir, no hay un barco ya puesto.
                    if cabe:
                        alrededor = self.casillas_alrededor(posiciones)

                        libre = True

                        for f, c in alrededor:
                            if self.tablero_propio[f][c] != agua:
                                libre = False
                                break
                    else:
                        libre = False

                    if libre:
                        # Colocamos el barco
                        for ilara, zutabe in posiciones:
                            self.tablero_propio[ilara][zutabe] = barco
                        
                        # Guardamos las posiciones de cada barco en una lista (esto nos ayuda luego para declarar cuando un barco está hundido)
                        self.itsasontzis.append(set(posiciones))
                        colocado = True

                    else:
                        continue

    def casillas_alrededor(self, posiciones):
        alrededor = set()

        for fila, columna in posiciones:
            for df in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    vecina_fila = fila + df
                    vecina_columna = columna + dc

                    if (0 <= vecina_fila < filas
                            and 0 <= vecina_columna < columnas):
                        alrededor.add((vecina_fila, vecina_columna))

        return alrededor

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