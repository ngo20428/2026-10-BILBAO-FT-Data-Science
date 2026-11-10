# funciones.py

import os
import shutil
from variables import DOWNLOADS_DIR, DESTINATIONS


def crear_directorios():

    for carpeta in DESTINATIONS.keys():
        ruta_carpeta = os.path.join(DOWNLOADS_DIR, carpeta)
        
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)


def clasificar_archivo(nombre_archivo):

    nombre_archivo_lower = nombre_archivo.lower()
    
    for carpeta, extensiones in DESTINATIONS.items():
        if nombre_archivo_lower.endswith(extensiones) and carpeta != 'Otros':
            return carpeta
            
    return 'Otros'

def organizar_carpeta_descargas():
    
    crear_directorios()

    for elemento in os.listdir(DOWNLOADS_DIR): # lista de los elementos en la carpeta de descargas
        ruta_elemento = os.path.join(DOWNLOADS_DIR, elemento) # ruta/dirección de cada elemento --> para poder acceder a él y moverlo
        
        if os.path.isfile(ruta_elemento):
                
            carpeta_destino = clasificar_archivo(elemento)
            ruta_destino = os.path.join(DOWNLOADS_DIR, carpeta_destino, elemento)

            try:
                shutil.move(ruta_elemento, ruta_destino)
                print(f"Movido con éxito: '{elemento}' -> Carpeta {carpeta_destino}")
            except Exception as e:
                print(f"Error al mover '{elemento}': {e}")
