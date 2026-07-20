# servirá para crear la conexión a BBDD 
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv() 

 ## crear el diccionario de conexion a base datos.
DB_CONFIG = {
    'host': os.getenv("MYSQL_LOCALHOST"),
    'port': int( os.getenv("MYSQL_PORT") ),
    'user': os.getenv("MYSQL_USER"),
    'password': os.getenv("MYSQL_PASSWORD"),
    'database': os.getenv("MYSQL_DATABASE")
}

def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Error: {e}")
        return None
    