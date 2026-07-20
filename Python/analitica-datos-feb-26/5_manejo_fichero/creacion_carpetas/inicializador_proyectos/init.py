import os

def init():
    try:
        # paso 0: crear la carpeta del proyecto
        os.makedirs('proyecto', exist_ok=True)
        # paso 1: crear fichero main.py vacio en la raiz
        fichero = open('./proyecto/main.py', 'w', encoding='UTF-8')
        fichero.close()
        # paso 2: crear la carpeta lib para la gestion de modulos.
        os.makedirs('./proyecto/lib', exist_ok=True)
        # paso 3: crear la carpeta data para la gestion de datos o fichero de datos.
        os.makedirs('./proyecto/data', exist_ok=True)
        print('#### PROYECTO CREADO CORRECTAMENTE ####')
    except:
        print('### HA HABIDO UN PROBLEMA NO SE HA CREADO EL PROYECTO ####')

init()