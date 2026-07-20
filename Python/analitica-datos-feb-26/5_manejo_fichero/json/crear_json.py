import json
import os

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_json(carpeta, fichero, datos):
    # crear la carpeta si no existe
    os.makedirs(carpeta, exist_ok=True)
    fichero = open(f"./{carpeta}/{fichero}", 'w', encoding='UTF-8')
    json.dump(datos, fichero, ensure_ascii=False, indent=4)
    fichero.close()


# crear_json('data', 'trabajadores.json', lista_empleados)