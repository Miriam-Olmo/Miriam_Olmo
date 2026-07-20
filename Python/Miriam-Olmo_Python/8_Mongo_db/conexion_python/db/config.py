# MongoClient me permite conectarme con Mongo
from pymongo import MongoClient
# load_dotenv cargar el fichero .env en este .py
from dotenv import load_dotenv
import os

# cargamos las variables de entorno
load_dotenv()

# extraemos la variables del fichero .env usando la libreria os
MONGO_URI = os.getenv("MONGO_URI" , 'mongodb://localhost:27017')
DB_NAME = os.getenv('MONGO_DB_NAME', "sismosdb")
COLLECTION_NAME = os.getenv('MONGO_COLLETION_NAME', 'sismos')

# dos pasos:
# 1 - paso, le doy a mongoclient la url de mi bbdd
client = MongoClient(MONGO_URI)

# 2a - crear un funcion que me permite conectarme a toda la BBDD
def get_conexion():
    return client[DB_NAME]

# 2b - la mas comun es conectar a bbdd y a la collection

def get_collection(collection=COLLECTION_NAME):
    return client[DB_NAME][collection]