# crear un excel con todos los datos del log, separador por item fecha...

# paso 1: leer el fichero y transformarlo en una lista de datos.
import os
from openpyxl import Workbook


def extraer_log(texto):
    valor = texto.split('=')
    return valor[1]

def leer_fichero(carpeta, archivo):
    ruta = f"./{carpeta}/{archivo}"
    fichero = open(ruta, 'r', encoding='UTF-8')
    lista = []
    for linea in fichero.readlines():
        linea.strip()
        if not linea:
            continue
        partes = linea.split(" ")
        
        # fecha es la union de los dos primeros items sin los []
        fecha_hora = f"{partes[0]} {partes[1]}".replace('[', '').replace(']','')
        ip = extraer_log(partes[2])
        metodo = extraer_log(partes[3])
        endpoint = extraer_log(partes[4])
        status = int(extraer_log(partes[5]))
        resp_time = int(extraer_log(partes[6]).replace('ms', '').replace('\n', ''))
        lista.append( [fecha_hora, ip, metodo, status, endpoint, resp_time] )
    fichero.close()
    return lista
# paso 2: crear fichero de excel desde una lista
# paso 3: transformar los datos.
def crear_excel(carpeta, archivo, datos):
    excel = Workbook()
    hoja= excel.active
    hoja.title= "Logs de server"
    cabeceras = ['fecha_hora', 'ip', 'metodo', 'status', 'endpoint', 'tiempo_respuesta']
    hoja.append(cabeceras)
    for fila in datos:
        hoja.append(fila)
    excel.save(f"./{carpeta}/{archivo}")
        


datos = leer_fichero('data', 'access_log.txt')
crear_excel('data', 'reporte_log.xlsx', datos)
    