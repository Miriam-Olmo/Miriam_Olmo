import xml.etree.ElementTree as et

lista_empleados = [
    {'id': 1, 'nombre': 'Juan Antonio', 'apellidos': 'Pérez Jarillo', 'correo': 'jj@gmail.com', 'departamento': 'Desarrollo' },
    {'id': 2, 'nombre': 'Almudena', 'apellidos': 'González Camuñas', 'correo': 'almu@gmail.com', 'departamento': 'Finanzas' },
    {'id': 3, 'nombre': 'Marta', 'apellidos': 'Rodriguez Lopez', 'correo': 'marta@gmail.com', 'departamento': 'Marketing' },
    {'id': 4, 'nombre': 'Joaquin', 'apellidos': 'Calvo Lopez', 'correo': 'joaquin@gmail.com', 'departamento': 'Finanzas' },
    {'id': 5, 'nombre': 'Lucia', 'apellidos': 'Pérez Alvárez', 'correo': 'lucia@gmail.com', 'departamento': 'Cuentas' },
]

def crear_xml(carpeta, fichero, datos):
    # paso 1: crear el nodo raiz
    nodo_raiz = et.Element('empleados') #<empleados></empleados>
    # paso 2: voy ha recorrer los datos para extraer la informacion
    for empleado in datos:
        # por cada empleado un nodo_hijo dentro de nodo_raiz
        nodo_empleado = et.SubElement(nodo_raiz, 'empleado', id=str(empleado['id'])) # <empleado id="1"></empleado>
        # nodo_nombre = et.SubElement(nodo_empleado, 'nombre') # <nombre></nombre>
        # nodo_apellidos = et.SubElement(nodo_empleado, 'apellidos') # <apellidos></apellidos>
        # nodo_correo = et.SubElement(nodo_empleado, 'correo') # <correo></correo>
        # nodo_departamento = et.SubElement(nodo_empleado, 'departamento') # <departamento></departamento>
        for key, value in empleado.items():
                if key != "id":
                    subelemento = et.SubElement(nodo_empleado, key)
                    subelemento.text = str(value)
    # paso 3: ya tengo todo el contenido dentro del nodo_raiz
    xml = et.ElementTree(nodo_raiz)
    xml.write(f"./{carpeta}/{fichero}", encoding='UTF-8', xml_declaration=True)

crear_xml('data','trabajadores.xml', lista_empleados)

crear_xml('data','trabajadores.xml', lista_empleados)


