from crear_json import crear_json
from leer_json import leer_json


def pedir_datos():
    nombre = input('Dime el nombre: ')
    apellidos = input('Dime el apellido: ')
    correo = input('Dime el correo: ')
    departamento = input('Dime el departamento: ')
    return {
        'nombre': nombre,
        'apellidos': apellidos,
        'correo': correo,
        'departamento': departamento
    }

def actualizar_json(carpeta, fichero):
    datos = leer_json(carpeta, fichero)
    ultimo_id = datos[-1]['id']
    nuevo_empleado = pedir_datos()
    nuevo_empleado = { 'id': ultimo_id + 1, **nuevo_empleado }
    datos.append(nuevo_empleado)
    crear_json(carpeta, fichero, datos)
    print('Empleado actualizado correctamente')

actualizar_json('data', 'empleados.json')