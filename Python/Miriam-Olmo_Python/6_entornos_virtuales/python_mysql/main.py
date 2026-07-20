import mysql.connector
from mysql.connector import Error
import pandas as pd
# configurar nuestra conexion

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'V4ll3c4n@93',
    'database': 'tinta_eterna'
}

def get_connection():
    try:
        return mysql.connector.connect(**db_config)
    except Error as E:
        print(f'Error: {E}')
        return None
    

# obtener listado con todos los libros

def get_all_books():
    try:
        # lo primero sera conectarse a la base
        conection = get_connection()
        # hacer consulta
        cursor = conection.cursor(dictionary=True)
        cursor.execute('select * from libros')
        return cursor.fetchall()
    except Error as E:
        print(f'Error: {E}')
        return []
    finally:
        conection.close()

# libros = get_all_books()
# print(libros)


# voy a hacer una peticion de un libro por id
def get_book_by_id(id_libro):
    try:
        conection = get_connection()
        cursor = conection.cursor(dictionary=True)
        cursor.execute(f'select * from libros where id=%s', (id_libro,))
        return cursor.fetchone()
    except Error as E:
        print(f'Error: {E}')
        return None
    finally:
        conection.close()

# libro_1 = get_book_by_id(12)
# print(libro_1)

# una funcion  que me permita obtener libros de un genero determinado

def get_book_by_gender(genero):
    try:
    # lo primero sera conectarse a la bbdd
        conn = get_connection()
        # hacer la consulta
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'select * from libros where genero=%s',(genero,))
        return cursor.fetchall()
    except Error as e:
        print(f'error: {e}')    
        return None
    finally:
        conn.close()



# libros_genero = get_book_by_gender('realismo magico')
# df = pd.DataFrame(libros_genero)
# print(df)

#dataframe de libros que cuesten entre 10 y 20€

def get_books_by_price(price_min, price_max, tipo):
    if price_min > price_max:
        return 'El precio minimo no puede ser mayor que el maximo'
    orden = "DESC" if tipo == 1 else "ASC"
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT * FROM libros WHERE precio BETWEEN %s AND %s ORDER BY precio {orden}', (price_min, price_max))
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()
        

# libros_precio_10_20 = get_books_by_price(40, 10, 2)
# if type(libros_precio_10_20) is str:
#     print(libros_precio_10_20)
# elif len(libros_precio_10_20) == 0:
#     print('No hay libros en eso precios')
# else:
#     df = pd.DataFrame(libros_precio_10_20)
#     print(df)

# devolver un dataframe conel titulo y el año de publicacion de los libros que esten publicados desde el 2000 en adelante y que tengand 300 o mas paginas

def get_books_by_year_page(year, page):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f'SELECT titulo, anyo_publicacion, paginas FROM libros WHERE anyo_publicacion >= %s and paginas >= %s ', (year, page))
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()

# libros_año_paginas = get_books_by_year_page(2000, 300)
# df = pd.DataFrame(libros_año_paginas)
# print(df)

# Top 5 libros más vendidos por número de compras. sacar titulo y genero


def get_books_by_top(top):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
                       select l.titulo, l.genero, count(c.id) as compras
                       from libros l
                       join compras c on l.id = c.libro_id
                       group by l.id
                       order by count(c.id) desc, l.id asc
                       limit %s
                       """, (top,))
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []
    finally:
        conn.close()

# top_ventas = get_books_by_top(15)
# df = pd.DataFrame(top_ventas)
# print(df)

# borrado compra de un libro por id o isbn

def delete_compra_by_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('delete from compras where id=%s', (id,))
        conn.commit()
        ## recomendable
        return 'compra borrada correctamente' if cursor.rowcount > 0 else 'no se ha podido borrar la compra, intentalo de nuevo'
    except Error as e:
        print(f'Error : {e}')
        return False
    
    finally:
        conn.close()

# rs = delete_compra_by_id(16)
# print(rs)

# insercion de un libro en la tabla libros

def insert_book(book):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""INSERT INTO libros 
                       (titulo, 
                       anyo_publicacion, 
                       isbn, 
                       genero, 
                       idioma, 
                       paginas, 
                       precio, 
                       editorial_id) 
                       VALUES 
                       (%s,%s,%s,%s,%s,%s,%s,%s)""", (
                           book['titulo'],
                           book['anyo_publicacion'],
                           book['isbn'],
                           book['genero'],
                           book['idioma'],
                           book['paginas'],
                           book['precio'],
                           book['editorial_id']
                           )
                       )
        conn.commit()
        # para sacar el libro que acabo de insertar necesito el id, para consultar por get_by_id
        lastid = cursor.lastrowid
        result = get_book_by_id(lastid)
        return result
    except Error as e:
        print(f'Error: {e}')
        return None
    finally:
        conn.close()
        

new_book = {
    'titulo': 'Los renglones torcidos de dios',
    'anyo_publicacion': 1990,
    'isbn': "978-8426344647",
    'genero': 'Drama',
    'idioma': 'Español',
    'paginas': 125,
    'precio': 10,
    'editorial_id': 2
}

# result = insert_book(new_book)
# print(result)

# actualizar los campos de un libro

def update_book(book):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('UPDATE libros SET titulo=%s, anyo_publicacion=%s, isbn=%s, genero=%s, idioma=%s, paginas=%s, precio=%s, editorial_id=%s WHERE id=%s', (
            book['titulo'],
            book['anyo_publicacion'],
            book['isbn'],
            book['genero'],
            book['idioma'],
            book['paginas'],
            book['precio'],
            book['editorial_id'],
            book['id'],
        ))
        conn.commit()
        result = get_book_by_id(book['id'])
        return result
    except Error as e:
        print(f'Error: {e}')
        return None
    finally:
        conn.close()
        

book_update = {
    'id': 41,
    'titulo': 'Los renglones torcidos de dios',
    'anyo_publicacion': 1985,
    'isbn': "978-8426344647",
    'genero': 'Drama',
    'idioma': 'Español',
    'paginas': 250,
    'precio': 15,
    'editorial_id': 1
}

result = update_book(book_update)
print(result)


