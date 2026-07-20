# ============================================
# LIB/EXPORTACION.PY
# ============================================

import csv

from openpyxl import Workbook

# ============================================
# EXPORTAR CSV
# ============================================

def exportar_csv(
    lista_datos,
    ruta_archivo
):

    if len(lista_datos) == 0:

        return

    archivo = open(

        ruta_archivo,

        mode="w",

        newline="",

        encoding="utf-8"
    )

    try:

        escritor_csv = csv.DictWriter(

            archivo,

            fieldnames=lista_datos[0].keys()
        )

        escritor_csv.writeheader()

        escritor_csv.writerows(
            lista_datos
        )

    finally:

        archivo.close()

# ============================================
# CREAR LIBRO EXCEL
# ============================================

def crear_libro_excel():

    return Workbook()

# ============================================
# ELIMINAR HOJA VACÍA
# ============================================

def eliminar_hoja_inicial(
    libro_excel
):

    hoja_inicial = libro_excel.active

    libro_excel.remove(
        hoja_inicial
    )

# ============================================
# CREAR HOJA
# ============================================

def crear_hoja_excel(
    libro_excel,
    nombre_hoja
):

    return libro_excel.create_sheet(
        title=nombre_hoja
    )

# ============================================
# OBTENER COLUMNAS
# ============================================

def obtener_columnas(
    lista_datos
):

    return list(
        lista_datos[0].keys()
    )

# ============================================
# ESCRIBIR COLUMNAS
# ============================================

def escribir_columnas_excel(
    hoja_excel,
    columnas
):

    hoja_excel.append(
        columnas
    )

# ============================================
# ESCRIBIR FILAS
# ============================================

def escribir_filas_excel(
    hoja_excel,
    lista_datos,
    columnas
):

    for fila in lista_datos:

        valores_fila = []

        for columna in columnas:

            valores_fila.append(
                fila[columna]
            )

        hoja_excel.append(
            valores_fila
        )

# ============================================
# EXPORTAR EXCEL
# ============================================

def exportar_excel(
    diccionario_datos,
    ruta_archivo
):

    libro_excel = crear_libro_excel()

    eliminar_hoja_inicial(
        libro_excel
    )

    for nombre_hoja, lista_datos in diccionario_datos.items():

        hoja_excel = crear_hoja_excel(

            libro_excel,

            nombre_hoja
        )

        if len(lista_datos) == 0:

            continue

        columnas = obtener_columnas(
            lista_datos
        )

        escribir_columnas_excel(

            hoja_excel,

            columnas
        )

        escribir_filas_excel(

            hoja_excel,

            lista_datos,

            columnas
        )

    libro_excel.save(
        ruta_archivo
    )

# ============================================
# ESCRIBIR INFORMACIÓN
# ============================================

def escribir_linea(
    archivo,
    texto
):

    archivo.write(
        texto + "\n"
    )

# ============================================
# EXPORTAR INFORME
# ============================================

def guardar_informe(
    auditorias
):

    archivo = open(

        "datos_limpios/informe_limpieza.txt",

        mode="w",

        encoding="utf-8"
    )

    try:

        escribir_linea(
            archivo,
            "=================================="
        )

        escribir_linea(
            archivo,
            "INFORME DE LIMPIEZA DE DATOS"
        )

        escribir_linea(
            archivo,
            "=================================="
        )

        escribir_linea(
            archivo,
            ""
        )

        for nombre_archivo, auditoria in auditorias.items():

            escribir_linea(
                archivo,
                f"ARCHIVO: {nombre_archivo}"
            )

            escribir_linea(
                archivo,
                f"TOTAL REGISTROS: "
                f"{auditoria['total_registros']}"
            )

            escribir_linea(
                archivo,
                f"DUPLICADOS: "
                f"{auditoria['duplicados']}"
            )

            escribir_linea(
                archivo,
                ""
            )

            escribir_linea(
                archivo,
                "VALORES VACÍOS:"
            )

            for campo, cantidad in auditoria[
                "valores_vacios"
            ].items():

                escribir_linea(

                    archivo,

                    f"{campo}: {cantidad}"
                )

            escribir_linea(
                archivo,
                ""
            )

            escribir_linea(
                archivo,
                "ESPACIOS EXTRA:"
            )

            for campo, cantidad in auditoria[
                "espacios_extra"
            ].items():

                escribir_linea(

                    archivo,

                    f"{campo}: {cantidad}"
                )

            escribir_linea(
                archivo,
                ""
            )

            escribir_linea(
                archivo,
                "----------------------------------"
            )

            escribir_linea(
                archivo,
                ""
            )

    finally:

        archivo.close()