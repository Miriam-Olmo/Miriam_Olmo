# exportamos a main para la carga de funciones y archivos
from lib.carga import cargar_csv, cargar_json, cargar_xml, cargar_excel
from lib.limpieza import limpiar_registros

artistas = cargar_csv('./datos/artistas.csv')
escenarios = cargar_excel('./datos/escenarios_horarios.xlsx')
patrocinadores = cargar_xml('./datos/patrocinadores.xml')
ventas = cargar_json('./datos/ventas_entradas.json')

# print(artistas)
# print('='*30)
# print(escenarios)
# print('='*30)
# print(patrocinadores)
# print('='*30)
# print(ventas)

""" 
====================================
nombre del fichero:
====================================
numero total de registros:
====================================
nombre de los campos/columnas:
====================================
5 primeros registros:
====================================
"""

# --- Aplicar la limpieza a los 4 ficheros ---
artistas       = limpiar_registros(artistas)
escenarios     = limpiar_registros(escenarios)
patrocinadores = limpiar_registros(patrocinadores)
ventas         = limpiar_registros(ventas)


def mostrar_info(nombre, datos):
    
    print("Nombre del fichero:", nombre)

    # número de registros
    print("Número total de registros:", len(datos))

    # nombres de campos
    print("Campos:", list(datos[0].keys()))

    # primeros 5 registros
    print("Primeros 5 registros:")
    for registro in datos[:5]:
        print(registro)

    print("=" * 40)


mostrar_info("artistas.csv", artistas)
mostrar_info("escenarios_horarios.xlsx", escenarios)
mostrar_info("patrocinadores.xml", patrocinadores)
mostrar_info("ventas_entradas.json", ventas)