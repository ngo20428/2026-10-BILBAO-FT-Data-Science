# variables.py

import os

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
software_types = ('.exe', '.py','.ipynb')


DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads') # os.path.expanduser('~') obtiene la ruta del directorio principal (home) del usuario --> e.g. C:\Users\NombreUsuario

# Diccionario para mapear cada categoría con su nombre de carpeta destino
DESTINATIONS = {
    'Documentos': doc_types,
    'Imagenes': img_types,
    'Software': software_types,
    'Otros': ()
}