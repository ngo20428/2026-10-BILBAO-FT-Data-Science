# FUNCIONES

def coordenadas():

    try:
        fila = int(input("Introduce la fila (0-9)"))
        columna = int(input("Introduce la columna (0-9)"))

        if 0 <= fila <= 9 and 0 <= columna <= 9:
            return fila, columna
        else:
            print("Error. Las coordenadas tienen que estar entre 0 y 9.")

    except Exception as e:
        print("Porfi, introducelo en númerico :)")


