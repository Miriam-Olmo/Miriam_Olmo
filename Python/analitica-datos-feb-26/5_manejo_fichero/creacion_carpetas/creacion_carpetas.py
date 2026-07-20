import os

def crear_archivo(carpeta, nombre, ext):
    ## os hay una funcion que me permite crear directorios.
    os.makedirs(carpeta, exist_ok=True)
    fichero = open(f"./{carpeta}/{nombre}.{ext}", "w", encoding="UTF-8")
    fichero.write('algo')
    fichero.close()
    
    
crear_archivo('data', 'prueba', 'txt')