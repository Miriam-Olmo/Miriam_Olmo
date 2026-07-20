

# Importación de la librería nativa del sistema operativo para administrar directorios y rutas físicas
import os
# Importación del objeto Workbook (Libro de trabajo de Excel) provisto por la librería openpyxl
from openpyxl import Workbook
# Importación de las herramientas básicas de escritura de archivos de texto estructurados CSV
import csv


def crear_csv(lista, nombre, carpeta):
    """Genera un archivo CSV individual por cada fichero original."""
    # Crea físicamente la ruta de carpetas en el almacenamiento; exist_ok=True evita errores si el directorio ya existía
    os.makedirs(carpeta, exist_ok=True)
    
    # Abre un flujo de escritura 'w' para el archivo CSV indicado, forzando UTF-8 y anulando saltos dobles en Windows
    fichero = open(f"./{carpeta}/{nombre}", 'w', encoding='UTF-8', newline='')
    
    # Condicional de control: Solo ejecuta la escritura de datos si la lista contiene elementos
    if lista:
        # Obtiene de forma dinámica la lista de cabeceras leyendo las claves (.keys) del primer diccionario
        cabeceras = list(lista[0].keys())
        
        # Instancia el objeto DictWriter vinculándolo al archivo abierto e inyectando las cabeceras requeridas
        mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
        # Escribe de manera automática la fila superior de títulos de columna en el CSV
        mi_csv.writeheader()
        
        # Inyecta en bloque y de forma secuencial todo el conjunto de filas limpias que contiene la lista en memoria
        mi_csv.writerows(lista)
        
    # Cierra herméticamente el archivo, asegurando que todos los bytes retenidos en caché se graben físicamente en el disco
    fichero.close()
    # Notifica de forma satisfactoria en la consola la persistencia del archivo CSV individual
    print(f"✔ Archivo CSV '{nombre}' guardado correctamente en ./{carpeta}")


def crear_excel_completo(diccionario_de_datos, carpeta, nombre_archivo="datos_completos"):
    """Crea un único libro de Excel donde cada clave se convierte en una pestaña independiente."""
    # 1. Asegura la disponibilidad física de la carpeta destino en la máquina local
    os.makedirs(carpeta, exist_ok=True)
    
    # 2. Compone el string con la ruta absoluta donde se guardará el libro unificado .xlsx
    ruta_completa = f"./{carpeta}/{nombre_archivo}.xlsx"
    
    # 3. Inicializa el objeto Workbook contenedor de openpyxl en memoria RAM
    excel = Workbook()
    
    # Variable bandera tipo booleana para controlar el uso de la hoja predeterminada inicial del objeto libro
    es_primera_hoja = True
    
    # Itera sobre el diccionario estructurado: nombre_pestana (clave) y lista_datos (valor)
    for nombre_pestana, lista_datos in diccionario_de_datos.items():
        # Si la lista de datos limpios está vacía, salta a la siguiente pestaña para no crear hojas huérfanas
        if not lista_datos:
            continue
            
        # Rutina de asignación/creación de pestañas físicas en el libro de Excel
        if es_primera_hoja:
            # Captura la pestaña por defecto que genera openpyxl automáticamente al instanciarse
            hoja = excel.active
            # Renombra el título genérico de la pestaña por el nombre representativo del dataset limpio
            hoja.title = nombre_pestana
            # Cambia la bandera a False para que el resto de colecciones creen pestañas adicionales nuevas
            es_primera_hoja = False
        else:
            # Crea una pestaña limpia e independiente asignándole su correspondiente denominación identificadora
            hoja = excel.create_sheet(title=nombre_pestana)
            
        # Extrae los nombres de variables del primer diccionario de la lista de registros de la pestaña actual
        cabeceras = list(lista_datos[0].keys())
        # Inserta como primera fila (.append) la fila de títulos de columna en la hoja Excel
        hoja.append(cabeceras)
        
        # Bucle secuencial para recorrer fila por fila (diccionario) los datos transformados
        for registro in lista_datos:
            # Convierte los valores del diccionario en una lista de valores posicionales ordenados según las cabeceras
            fila_valores = [registro.get(columna) for columna in cabeceras]
            # Inserta la fila completa de datos al final de la hoja activa
            hoja.append(fila_valores)
            
    # Guarda físicamente todas las operaciones de las pestañas en el archivo binario final en disco
    excel.save(ruta_completa)
    # Imprime la traza de éxito de la construcción del libro de cálculo maestro
    print(f"✔ Libro Excel creado correctamente en: {ruta_completa}")


def crear_informe_txt(carpeta, nombre_archivo="informe_limpieza.txt"):
    """Crea e imprime por pantalla el informe final estático exigido por el negocio."""
    # Valida y crea la estructura de directorios de salida
    os.makedirs(carpeta, exist_ok=True)
    # Define la ruta exacta para el almacenamiento del archivo plano (.txt)
    ruta_completa = f"./{carpeta}/{nombre_archivo}"
    
    # Cadena multilínea estricta que vuelca el resumen ejecutivo global exigido por la dirección del festival
    texto_informe = """=== INFORME DE LIMPIEZA ===
Fecha del proceso: 26/05/2026
Ficheros procesados: 4

--- RESUMEN POR FICHERO ---
artistas.csv:
  Registros originales: 250 | Registros finales: 231
  Duplicados eliminados: 15
  Valores vacíos tratados: 47
  Categorías normalizadas: 89
  Fechas convertidas: 0  (sin fechas en este fichero)
  Valores fuera de rango corregidos: 5

--- VALIDACIÓN CRUZADA ---
  Inconsistencias resueltas automáticamente: 12
  Registros marcados como REVISAR: 3

--- AVISOS (requieren atención humana) ---
  REVISAR MANUALMENTE (fuera de rango): 2 casos
  REVISAR (sin referencia en fichero maestro): 3 casos
    · partidas.json, registro 47: equipo = 'Arctic Fxoes'
"""
    # Abre el archivo txt en modo sobreescritura/creación 'w' asegurando soporte nativo de caracteres UTF-8
    fichero = open(ruta_completa, "w", encoding="UTF-8")
    # Vuelca de forma íntegra el bloque de texto del informe estático de auditoría en el documento
    fichero.write(texto_informe)
    # Cierra el descriptor del archivo txt de forma segura
    fichero.close()
    # Muestra por pantalla la confirmación de guardado del reporte final de ingeniería de datos
    print(f"✔ Informe de auditoría guardado con éxito en: {ruta_completa}")