# Tienes una lista de ventas con los campos:
#   id, fecha, producto, categoria, cantidad, precio_unitario, vendedor, region
# El objetivo del ejercio es conseguir una hoja excel con esos datos.
# este excel tiene que tener una columna nueva. total = cantidad * precio_unitario
import os 
from openpyxl import Workbook

ventas = [
    {'id':1,  'fecha':'2026-01-15', 'producto':'Laptop Pro',     'categoria':'Electrónica', 'cantidad':2, 'precio_unitario':899.00, 'vendedor':'Ana García',   'region':'Norte'},
    {'id':2,  'fecha':'2026-01-16', 'producto':'Ratón WiFi',      'categoria':'Periféricos', 'cantidad':10,'precio_unitario': 14.99, 'vendedor':'Luis Martínez','region':'Sur'},
    {'id':3,  'fecha':'2026-01-17', 'producto':'Monitor 24"',     'categoria':'Electrónica', 'cantidad':5, 'precio_unitario':249.00, 'vendedor':'Ana García',   'region':'Norte'},
    {'id':4,  'fecha':'2026-01-18', 'producto':'Teclado Mecánico','categoria':'Periféricos', 'cantidad':8, 'precio_unitario': 64.99, 'vendedor':'Marta Pérez',  'region':'Este'},
    {'id':5,  'fecha':'2026-01-19', 'producto':'Webcam HD',       'categoria':'Periféricos', 'cantidad':15,'precio_unitario': 25.00, 'vendedor':'Luis Martínez','region':'Sur'},
    {'id':6,  'fecha':'2026-01-20', 'producto':'Laptop Pro',      'categoria':'Electrónica', 'cantidad':3, 'precio_unitario':899.00, 'vendedor':'Marta Pérez',  'region':'Este'},
    {'id':7,  'fecha':'2026-01-21', 'producto':'Auriculares BT',  'categoria':'Electrónica', 'cantidad':7, 'precio_unitario': 79.99, 'vendedor':'Javier Ruiz',  'region':'Oeste'},
    {'id':8,  'fecha':'2026-01-22', 'producto':'Monitor 24"',     'categoria':'Electrónica', 'cantidad':2, 'precio_unitario':249.00, 'vendedor':'Javier Ruiz',  'region':'Oeste'},
]

def generar_excel_ventas(carpeta, fichero, datos):
    # paso 1: crear la carpeta donde voy a guardar el excel
    os.makedirs(carpeta, exist_ok=True)
    # ruta del documento.
    ruta = f"./{carpeta}/{fichero}"
    
    #inicilizar el libro de excel
    excel = Workbook()
    hoja = excel.active
    hoja.title = "Registro de ventas"
    
    # extraer las cabeceras del primer diccionario para pintarlas en el excel.
    cabeceras = list(datos[0].keys())
    cabeceras.append('total')
    hoja.append(cabeceras)
    
    # vamos a insertar un registro por diccionario.
    for producto in datos:
        producto['total'] = producto['cantidad'] * producto['precio_unitario']
        fila = [producto[clave] for clave in cabeceras]
        hoja.append(fila)
    
    excel.save(ruta)
    print('Fichero creado correctamente')

generar_excel_ventas('data', 'ventas.xlsx', ventas)