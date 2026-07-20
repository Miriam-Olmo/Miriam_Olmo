from openpyxl import Workbook

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'departamento': 'Cuentas' , 'id': 5, 'apellidos': 'Pérez Alvárez', 'nombre': 'Lucia', 'correo': 'lucia@gmail.com', },
]

def crear_excel(carpeta, fichero, datos):
    # crear primero el libro de excel
    wb = Workbook()
    # seleccionamos al primera hoja
    hoja = wb.active
    hoja.title = 'Empleados'
    
    # extraer de un diccionario cualquier de mi lista las cabeceras.
    cabeceras = list(datos[0].keys())
    # quiero añadirlo a mi hoja
    hoja.append(cabeceras)
    
    # recorremos nuestra de lista de datos para imprimir en cada fila un dato concreto
    for empleado in datos:
        # para que esto funcione el empleado tiene que tener los datos en el mismo orden que la lista caberas. Y estar convertido en lista.
        # lista_empleado = list(empleado.values())
        lista_empleado = [empleado[clave] for clave in cabeceras ]
        hoja.append(lista_empleado)
    
    wb.save(f'./{carpeta}/{fichero}')


crear_excel('data', 'trabajadores.xlsx', lista_empleados)