import csv
import os

import openpyxl


def exportar_csv(datos, ruta):
    if not datos:
        return
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=datos[0].keys())
        writer.writeheader()
        writer.writerows(datos)


def exportar_excel(hojas, ruta):
    """hojas: dict {nombre_hoja: lista_de_dicts}"""
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    for nombre, datos in hojas.items():
        ws = wb.create_sheet(nombre[:31])
        if not datos:
            continue
        cabeceras = list(datos[0].keys())
        ws.append(cabeceras)
        for reg in datos:
            ws.append([reg.get(c) for c in cabeceras])
    wb.save(ruta)


def guardar_informe(texto, ruta):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(texto)
    print(texto)
