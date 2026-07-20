# creacion de carpeta datos limpios con csv, excel, json,xml
import os
from openpyxl import Workbook
import csv



def crear_csv(lista, nombre, carpeta):
    """Genera un archivo CSV individual por cada fichero original"""
    os.makedirs(carpeta, exist_ok=True)
    
    fichero = open(f"./{carpeta}/{nombre}", 'w', encoding='UTF-8', newline='')
    
    if lista:
        # Extraemos las cabeceras de las llaves del diccionario
        cabeceras = list(lista[0].keys())
        
        mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
        mi_csv.writeheader()
        
        # escribe todas las filas con los datos limpios
        mi_csv.writerows(lista)
        
    fichero.close()
    print(f"✔ Archivo CSV '{nombre}' guardado correctamente en ./{carpeta}")



def crear_excel_completo(diccionario_de_datos, carpeta_destino, nombre_archivo="datos_completos"):
    os.makedirs(carpeta_destino, exist_ok=True)
    ruta = f"./{carpeta_destino}/{nombre_archivo}.xlsx"
    
    libro = Workbook()
    libro.remove(libro.active)
    
    for nombre_hoja, datos in diccionario_de_datos.items():
        if not datos:
            continue
        hoja = libro.create_sheet(title=nombre_hoja)
        cabeceras = list(datos[0].keys())
        hoja.append(cabeceras)
        for fila in datos:
            hoja.append([fila[columna] for columna in cabeceras])
            
    libro.save(ruta)
    print(f"✔ Libro Excel maestro creado correctamente en: {ruta}")

def crear_informe_txt(carpeta_destino, metricas_procesamiento, nombre_archivo="informe_limpieza.txt"):
    os.makedirs(carpeta_destino, exist_ok=True)
    ruta_completa = f"./{carpeta_destino}/{nombre_archivo}"
    
    lineas_informe = [
        "=== INFORME DE LIMPIEZA ===",
        "Fecha del proceso: 26/05/2026",
        f"Ficheros procesados: {len(metricas_procesamiento)}",
        "\n--- RESUMEN POR FICHERO ---"
    ]
    
    for fichero, info in metricas_procesamiento.items():
        lineas_informe.extend([
            f"{fichero}:",
            f"  Registros originales: {info['originales']} | Registros finales: {info['finales']}",
            f"  Duplicados eliminados: {info['duplicados']}",
            f"  Valores vacíos tratados: {info['vacios']}",
            f"  Categorías normalizadas: {info['categorias']}",
            f"  Fechas convertidas: {info['fechas']}"
        ])
        
    lineas_informe.extend([
        "\n--- VALIDACIÓN CRUZADA ---",
        "  Fases 8 y 9 desactivadas por especificación del usuario.",
        "\n--- AVISOS (requieren atención humana) ---",
        "  Ninguno (Procesamiento cruzado omitido)."
    ])
    
    texto_informe_completo = "\n".join(lineas_informe)
    print("\n" + texto_informe_completo)
    
    fichero = open(ruta_completa, "w", encoding="UTF-8")
    fichero.write(texto_informe_completo + "\n")
    fichero.close()