import csv

def extraer_ultimo_id(carpeta, nombre):
    fichero = open(f'./{carpeta}/{nombre}', 'r', encoding='UTF-8')
    datos = list( csv.DictReader(fichero) )
    fichero.close()
    return int(datos[-1]['id']) + 1
    
def pedir_datos():
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    correo = input("Correo: ")
    dpto = input('Departamento: ')
    return [nombre,apellidos ,correo, dpto]

def actualizar_datos(carpeta, nombre):
    try:
        empleado_nuevo = pedir_datos()
        # añadir el siguiente id al nuevo empleado
        empleado_nuevo.insert(0, extraer_ultimo_id(carpeta, nombre)) 
        fichero = open(f"./{carpeta}/{nombre}", 'a', encoding='UTF-8', newline="")
        mi_csv = csv.writer(fichero)
        mi_csv.writerow(empleado_nuevo)
        print('El archivo ha sido actualizado')
        fichero.close()
    except:
        print('El archivo no ha podido actualizarse')
  
    
actualizar_datos('data', 'empleados.csv')

