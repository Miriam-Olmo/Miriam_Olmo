# objetivo del ejercicio es guardar los datos de los alumnos aprobados y suspensos en dos fichero json llamados aprobados.json y suspensos.json dentro de una carpeta data que no podemos crear manualmente
import json
import os
lista_alumnos = [
    {'nombre': 'Carlos Rodríguez', 'nota': 2.0, 'aprobado': False},
    {'nombre': 'Pedro Gómez', 'nota': 3.5, 'aprobado': False},
    {'nombre': 'Marta Fernández', 'nota': 7.6, 'aprobado': False},
    {'nombre': 'Luis Martínez', 'nota': 1.6, 'aprobado': False},
    {'nombre': 'Diego Ruiz', 'nota': 3.1, 'aprobado': False},
    {'nombre': 'Ana Pérez', 'nota': 5.2, 'aprobado': True},
    {'nombre': 'Elena Rodríguez', 'nota': 1.1, 'aprobado': False},
    {'nombre': 'Sofía Pérez', 'nota': 3.0, 'aprobado': False},
    {'nombre': 'María Ruiz', 'nota': 5.7, 'aprobado': True},
    {'nombre': 'Pedro López', 'nota': 2.2, 'aprobado': False},
    {'nombre': 'Pablo Ruiz', 'nota': 3.6, 'aprobado': False},
    {'nombre': 'Javier Ruiz', 'nota': 8.6, 'aprobado': True},
    {'nombre': 'María Gómez', 'nota': 3.2, 'aprobado': False},
    {'nombre': 'Carlos Ruiz', 'nota': 4.1, 'aprobado': False},
    {'nombre': 'Ana Ruiz', 'nota': 5.4, 'aprobado': True},
    {'nombre': 'Carlos Gómez', 'nota': 8.6, 'aprobado': True},
    {'nombre': 'Javier Gómez', 'nota': 5.3, 'aprobado': True},
    {'nombre': 'Javier Sánchez', 'nota': 9.2, 'aprobado': True},
    {'nombre': 'Carlos Fernández', 'nota': 5.6, 'aprobado': True},
    {'nombre': 'Marta Gómez', 'nota': 8.0, 'aprobado': True},
    {'nombre': 'Pablo Martínez', 'nota': 5.6, 'aprobado': True},
    {'nombre': 'María Gómez', 'nota': 6.0, 'aprobado': True},
    {'nombre': 'Lucía Sánchez', 'nota': 2.3, 'aprobado': False},
    {'nombre': 'Sofía Sánchez', 'nota': 5.9, 'aprobado': True},
    {'nombre': 'María Martínez', 'nota': 7.9, 'aprobado': True},
    {'nombre': 'Carlos Pérez', 'nota': 4.9, 'aprobado': False},
    {'nombre': 'Carlos González', 'nota': 5.6, 'aprobado': True},
    {'nombre': 'Lucía Gómez', 'nota': 6.0, 'aprobado': True},
    {'nombre': 'Elena Fernández', 'nota': 3.9, 'aprobado': False},
    {'nombre': 'Pablo Gómez', 'nota': 4.0, 'aprobado': False},
    {'nombre': 'Ana Martínez', 'nota': 1.6, 'aprobado': False},
    {'nombre': 'Carlos Martínez', 'nota': 8.6, 'aprobado': True},
    {'nombre': 'Pablo López', 'nota': 3.7, 'aprobado': False},
    {'nombre': 'Pablo Gómez', 'nota': 9.7, 'aprobado': True},
    {'nombre': 'Marta Fernández', 'nota': 8.8, 'aprobado': True},
    {'nombre': 'María Gómez', 'nota': 9.5, 'aprobado': True},
    {'nombre': 'Carlos López', 'nota': 7.0, 'aprobado': True},
    {'nombre': 'María Rodríguez', 'nota': 7.0, 'aprobado': True},
    {'nombre': 'Carlos Pérez', 'nota': 2.0, 'aprobado': False},
    {'nombre': 'Ana Sánchez', 'nota': 2.3, 'aprobado': False},
    {'nombre': 'Sofía García', 'nota': 1.3, 'aprobado': False},
    {'nombre': 'Elena Martínez', 'nota': 5.2, 'aprobado': True},
    {'nombre': 'Pedro Sánchez', 'nota': 5.3, 'aprobado': True},
    {'nombre': 'Pablo López', 'nota': 1.3, 'aprobado': False},
    {'nombre': 'Carlos Pérez', 'nota': 9.5, 'aprobado': True},
    {'nombre': 'Carlos Gómez', 'nota': 9.0, 'aprobado': True},
    {'nombre': 'Pedro Gómez', 'nota': 6.1, 'aprobado': True},
    {'nombre': 'Elena López', 'nota': 1.4, 'aprobado': False},
    {'nombre': 'Ana Fernández', 'nota': 3.9, 'aprobado': False},
    {'nombre': 'Carlos García', 'nota': 8.6, 'aprobado': True},
    {'nombre': 'Sofía Gómez', 'nota': 4.1, 'aprobado': False},
    {'nombre': 'Javier Ruiz', 'nota': 8.1, 'aprobado': True},
    {'nombre': 'Luis Ruiz', 'nota': 5.9, 'aprobado': True},
    {'nombre': 'Pablo Rodríguez', 'nota': 5.2, 'aprobado': True},
    {'nombre': 'Carlos Sánchez', 'nota': 1.9, 'aprobado': False},
    {'nombre': 'Luis Ruiz', 'nota': 1.8, 'aprobado': False},
    {'nombre': 'Diego López', 'nota': 8.2, 'aprobado': True},
    {'nombre': 'Elena Martínez', 'nota': 5.5, 'aprobado': True},
    {'nombre': 'Elena Gómez', 'nota': 7.5, 'aprobado': True},
    {'nombre': 'Elena Rodríguez', 'nota': 1.9, 'aprobado': False},
    {'nombre': 'Sofía Pérez', 'nota': 8.0, 'aprobado': True},
    {'nombre': 'Ana López', 'nota': 9.3, 'aprobado': True},
    {'nombre': 'Elena González', 'nota': 4.6, 'aprobado': False},
    {'nombre': 'Pablo González', 'nota': 9.3, 'aprobado': True},
    {'nombre': 'Luis Martínez', 'nota': 5.8, 'aprobado': True},
    {'nombre': 'Ana Rodríguez', 'nota': 5.3, 'aprobado': True},
    {'nombre': 'María Ruiz', 'nota': 5.6, 'aprobado': True},
    {'nombre': 'Pedro Martínez', 'nota': 4.4, 'aprobado': False},
    {'nombre': 'Diego González', 'nota': 8.5, 'aprobado': True},
    {'nombre': 'Pedro Ruiz', 'nota': 7.8, 'aprobado': True},
    {'nombre': 'Ana Fernández', 'nota': 8.5, 'aprobado': True},
    {'nombre': 'Javier Martínez', 'nota': 4.2, 'aprobado': False},
    {'nombre': 'Marta Fernández', 'nota': 4.9, 'aprobado': False},
    {'nombre': 'Pablo Gómez', 'nota': 5.7, 'aprobado': True},
    {'nombre': 'Diego Gómez', 'nota': 2.7, 'aprobado': False},
    {'nombre': 'Diego Fernández', 'nota': 6.0, 'aprobado': True},
    {'nombre': 'Ana Rodríguez', 'nota': 5.4, 'aprobado': True},
    {'nombre': 'Diego Ruiz', 'nota': 9.3, 'aprobado': True},
    {'nombre': 'Luis López', 'nota': 3.7, 'aprobado': False},
    {'nombre': 'Carlos Ruiz', 'nota': 3.7, 'aprobado': False},
    {'nombre': 'Diego López', 'nota': 6.8, 'aprobado': True},
    {'nombre': 'Pablo Gómez', 'nota': 1.7, 'aprobado': False},
    {'nombre': 'Carlos Gómez', 'nota': 4.3, 'aprobado': False},
    {'nombre': 'Lucía Sánchez', 'nota': 9.5, 'aprobado': True},
    {'nombre': 'Javier González', 'nota': 5.4, 'aprobado': True},
    {'nombre': 'Pablo Martínez', 'nota': 1.2, 'aprobado': False},
    {'nombre': 'Ana Ruiz', 'nota': 9.6, 'aprobado': True},
    {'nombre': 'Sofía Ruiz', 'nota': 8.9, 'aprobado': True},
    {'nombre': 'Luis Ruiz', 'nota': 7.3, 'aprobado': True},
    {'nombre': 'Ana González', 'nota': 3.3, 'aprobado': False},
    {'nombre': 'Marta Sánchez', 'nota': 3.0, 'aprobado': False},
    {'nombre': 'Pedro López', 'nota': 7.1, 'aprobado': True},
    {'nombre': 'Sofía Sánchez', 'nota': 2.3, 'aprobado': False},
    {'nombre': 'Diego Martínez', 'nota': 5.9, 'aprobado': True},
    {'nombre': 'Elena Gómez', 'nota': 1.9, 'aprobado': False},
    {'nombre': 'Pablo González', 'nota': 9.3, 'aprobado': True},
    {'nombre': 'Diego Martínez', 'nota': 8.3, 'aprobado': True},
    {'nombre': 'Ana López', 'nota': 5.9, 'aprobado': True},
    {'nombre': 'Marta Pérez', 'nota': 6.6, 'aprobado': True},
    {'nombre': 'Marta Sánchez', 'nota': 8.9, 'aprobado': True}
]


# paso 1: crear un funcion que pasandole datos genere un json me da igual los datos

def crear_json(datos, fichero, carpeta="data"):
    # Creamos la carpeta  si no existe.
    os.makedirs(carpeta, exist_ok=True)
    
    # construimos al ruta final del archivo
    ruta = f"./{carpeta}/{fichero}"
    fichero = open(ruta, 'w', encoding='UTF-8')
    json.dump(datos, fichero, ensure_ascii= False, indent=4)
    fichero.close()
    print('Fichero creado correctamente')


# paso 2: crear un funcion que me devuelva una lista de aprobados

def filtrar_alumnos_aprobados(datos):
    lista_filtrada = []
    for alumno in datos:
        if alumno['nota'] >= 5:
            alumno['aprobado'] = True
            lista_filtrada.append(alumno)
    return lista_filtrada

# paso 3: modificar la funcion anterior para que me valga para aprobados y y suspensos

def filtrar_alumnos(datos, notamin, notamax):
    lista_filtrada = []
    for alumno in datos:
        if alumno['nota'] >= notamin and alumno['nota'] <= notamax:
            alumno['aprobado'] = True if alumno['nota'] > 5 else False
            lista_filtrada.append(alumno)
    return lista_filtrada

lista = filtrar_alumnos(lista_alumnos, 4, 7)
crear_json(lista, 'otros.json', 'data')
lista_aprobados = filtrar_alumnos(lista_alumnos, 5, 10)
crear_json(lista_aprobados, 'aprobados.json', 'data')