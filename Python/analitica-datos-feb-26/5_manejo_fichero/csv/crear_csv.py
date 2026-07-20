import csv

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_csv(lista, nombre, carpeta):
    fichero = open(f"./{carpeta}/{nombre}", 'a', encoding='UTF-8', newline='')
    # saber las cabeceras.
    cabeceras = []
    for key in lista[0].keys():
        cabeceras.append(key)
    #volcar los datos de la lista en un objeto csv
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras) 
    #imprimir cabeceras en la primera linea
    mi_csv.writeheader()
    # Escribir cada fila en el csv
    mi_csv.writerows(lista_empleados)
    # cerramos el fichero
    fichero.close()
        
crear_csv(lista_empleados, 'trabajadores.csv', 'data')