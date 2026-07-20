# visualizar datos de forma facil con pandas
import pandas as pd
from db.config import get_connection 
from mysql.connector import Error
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)

def get_compra():
    try:
        # lo primero crear la conn
        conn = get_connection()
        # abrimos el sqlfile para hacer la consulta sql
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM productos')
        return cursor.fetchall()
    except Error as e:
        print(f"Error {e}")
    finally:
        conn.close()
        

def aplicar_color(prioridad):
    prioridad = prioridad.lower()
    if prioridad == 'alta':
        return f'{Fore.RED}{prioridad}{Style.RESET_ALL}'
    elif prioridad == 'media':
        return f'{Fore.YELLOW}{prioridad}{Style.RESET_ALL}'
    elif prioridad == 'baja':
        return f'{Fore.GREEN}{prioridad}{Style.RESET_ALL}'
    return prioridad


def pintar_compra(lista):
    if not lista or len(lista) == 0:
        print('no necesitamos nada, lista vacia')
    # un dataframe se maneja igual que un diccionario
    df = pd.DataFrame(lista)
    # voy a aplicar solo a la columna prioridad el color segun el texto almacenado
    if 'prioridad' in df.columns:
        df['prioridad'] = df['prioridad'].apply(aplicar_color)
        # añadir directamente a mi df una columna nueva
        df['precio_total'] = round(df['precio'] * df['cantidad'] * 1.21, 2)
    print(df.columns) # devuelve las cabeceras de las columnas
    print('-' * 30)
    print(' # lista productos # ')
    # funcion apply permite aplicar cierto tipo de funciones a la columna
    # headers=keys muestra el nombre de las columnas y showindex=false quita la posicion del dataframe
    print(tabulate(df, headers='keys')) 
    print('-' * 30)

def eliminar_articulo(id):
    try:
        # lo primero obtener la conexion
        conn = get_connection()
        # abrimos el sql
        cursor = conn.cursor()
        cursor.execute('delete from productos where id=%s', (id,))
        conn.commit()
        if cursor.rowcount>0:
            return f'el producto con id {id} ha sido eliminado'
        return 'no se ha podido eliminar el producto. id no encontrado'
    except Error as e:
        print(f'Error {e}')
    finally:
        conn.close()

def insertar_articulo(producto_tupla):
    try:
        # lo primero obtener la conexion
        conn = get_connection()
        # abrimos el sql
        cursor = conn.cursor()
        cursor.execute('insert to {producto_tupla} from productos where producto_tupla=%s', (producto_tupla,))
        conn.commit()
    except Error as e:
        print(f'Error {e}')
    finally:
        conn.close()
