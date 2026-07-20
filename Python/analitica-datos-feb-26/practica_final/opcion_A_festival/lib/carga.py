import csv
import json
import xml.etree.ElementTree as ET

import openpyxl


def cargar_csv(ruta):
    with open(ruta, encoding='utf-8') as f:
        return list(csv.DictReader(f))


def cargar_excel(ruta, hoja=0):
    wb = openpyxl.load_workbook(ruta)
    ws = wb.worksheets[hoja] if isinstance(hoja, int) else wb[hoja]
    filas = list(ws.iter_rows(values_only=True))
    if not filas:
        return []
    cabeceras = [str(c) if c is not None else f'col_{i}' for i, c in enumerate(filas[0])]
    return [
        dict(zip(cabeceras, fila))
        for fila in filas[1:]
        if any(v is not None for v in fila)
    ]


def cargar_json(ruta):
    with open(ruta, encoding='utf-8') as f:
        datos = json.load(f)
    return datos if isinstance(datos, list) else []


def cargar_xml(ruta, etiqueta):
    tree = ET.parse(ruta)
    return [
        {child.tag: child.text for child in elem}
        for elem in tree.getroot().findall(etiqueta)
    ]
