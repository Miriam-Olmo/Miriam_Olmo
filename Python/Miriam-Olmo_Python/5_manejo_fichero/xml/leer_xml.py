import xml.etree.ElementTree as et

def leer_xml(carpeta, fichero):
    # leer un archivo en bruto
    fichero = et.parse(f'./{carpeta}/{fichero}')
    # me devuelve el nodo principal
    nodo_raiz = fichero.getroot()

    lista_empleados = []

    for emp in nodo_raiz.findall('empleado'):
        # extraer la informacion del empleado y insertarla en diccionario empleado
        #print(emp.get('id'))
        #print(emp.find('nombre').text)
        empleado = {
            'id': emp.get('id'),
            'nombre': emp.find('nombre').text,
            'apellidos': emp.find('apellidos').text,
            'correo': emp.find('correo').text,
            'departamento': emp.find('departamento').text
        }
        lista_empleados.append(empleado)
    return lista_empleados
    
empleados = leer_xml('data', 'empleados.xml')