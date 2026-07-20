# para crear un fichero tenemos  bandera "w", si no existe fichero lo crea, si existe lo sobrescribe.

notas_modulo_python = [
    {'nombre': 'Paula', 'nota': 8},
    {'nombre': 'Pablo', 'nota': 3.5},
    {'nombre': 'Lara', 'nota': 4},
    {'nombre': 'Miguel Angel', 'nota': 6},
    {'nombre': 'Miriam', 'nota': 9},
    {'nombre': 'Reniel', 'nota': 6.5},
    {'nombre': 'David', 'nota': 3},
    {'nombre': 'Luis', 'nota': 6},
]


def crear_fichero(nombre_fichero, ruta, extension, datos):
    path = f"{ruta}{nombre_fichero}{extension}"
    fichero = open(path, 'w', encoding='UTF-8')
    # guardar los valores en mi fichero.
    for alumno in datos:
        fichero.write(f"{alumno['nombre']}: {alumno['nota']}\n")
    
    fichero.close()


crear_fichero('notas_python', './datos/', '.txt', notas_modulo_python)