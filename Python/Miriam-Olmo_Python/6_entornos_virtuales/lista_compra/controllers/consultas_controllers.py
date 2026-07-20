# visualizar datos de forma facil con pandas
import pandas as pd
from db.config import get_connection 
from mysql.connector import Error
from colorama import init, Fore, Style
from tabulate import tabulate

# inicializar colorama
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
        return f"{Fore.RED}{prioridad}{Style.RESET_ALL}" 
    elif prioridad == 'media':
        return f"{Fore.YELLOW}{prioridad}{Style.RESET_ALL}"
    elif prioridad == 'baja':
        return f"{Fore.GREEN}{prioridad}{Style.RESET_ALL}"
    return prioridad
    
    
def pintar_compra(list):
    if not list or len(list) == 0:
        print('No necesitamos nada, lista vacia')
        
    df = pd.DataFrame(list)
    # voy a aplicar solo a la columna prioridad el color segun el texto almacenado
    
    if 'prioridad' in df.columns:
        df['prioridad'] = df['prioridad'].apply(aplicar_color)
        
    # añadir directamente a mi df un columna nueva
    df['precio_total'] = df['precio'] * df['cantidad'] * 1.21
    
    print('-' * 30)
    print('# Lista Productos #')
    # header="keys" muestra el nombre de las columnas y showindex=False quita la posicion del dataframe
    print(tabulate(df, headers='keys', showindex=False))
    print('-' * 30)
    

def eliminar_articulo(id):
    try:
        
        # lo primero obtener la conexion
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM productos WHERE id=%s', (id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            return f"El producto con id {id} ha sido eliminado"
        return "No se ha podido eliminar el producto, id no encontrado"
        
    except Error as e:
        print(f"Error {e}")
    finally:
        conn.close()


def insertar_articulo(producto_tupla):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO productos (nombre, precio, cantidad, prioridad) VALUES (%s, %s, %s,%s)', producto_tupla)
        conn.commit()
        return 'Producto insertado correctamente'
    except Error as e:
        print(f"Error {e}")
    finally:
        conn.close()
        
        
def obtener_productos_prioridad(prioridad):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM productos WHERE prioridad=%s ORDER BY precio DESC", (prioridad,))
        return cursor.fetchall()
    except Error as e:
        print(f'Error: {e}')
    finally:
        conn.close()
