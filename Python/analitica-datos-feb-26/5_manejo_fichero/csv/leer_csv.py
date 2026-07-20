import csv

def pintar_datos(ruta, fichero):
    fichero = open(f'{ruta}/{fichero}', 'r', encoding='UTF-8')
    # crear un elemento lector que me va permitir leer csv
    lector = csv.reader(fichero)
    # si al archivo tiene cabeceras me las salto
    next(lector)
    for fila in lector:
        print('-' * 20)
        print(f"{fila[0]}: {fila[1]} {fila[2]} - Departamento: {fila[4]}")
    else:
        print('-' * 20)
    fichero.close()

#pintar_datos('data', 'empleados.csv')

## crear un funcion que extraiga del csv un lista de empleado
## [ {id:1, nombre: juanan, apellidos: perez, departamento: desarrollo, correo: jj@gmail.com}, {id:1, nombre: lucia, apellidos: martin, departamento: desarrollo, correo: jj@gmail.com} ]

def cargar_datos(carpeta, fichero):
    fichero = open(f"{carpeta}/{fichero}", "r", encoding='UTF-8')
    lector = csv.reader(fichero)
    lista_empleados = []
    next(lector)
    for fila in lector:
        empleado = {
            'id': fila[0],
            'nombre': fila[1],
            'apellidos': fila[2],
            'departamento': fila[4],
            'correo': fila[3]
        }
        lista_empleados.append(empleado)
    print(lista_empleados)
    fichero.close()
    return lista_empleados
    
def cargar_datos2(carpeta, fichero):
    fichero = open(f"{carpeta}/{fichero}", "r", encoding='UTF-8')
    lector = csv.DictReader(fichero) 
    lista_empleados = list(lector)
    print(lista_empleados)
    fichero.close()
    
    

    
cargar_datos2('data', 'empleados.csv')  