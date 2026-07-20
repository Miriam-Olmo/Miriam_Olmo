"""
tres acciones para realizar con un fichero
open.
    r(read) -> leer fichero, extraer pero no puedo modificarlo
    w(write) -> sobreescribirlo, es decir lo que tenga se borrar
    a(append) -> añadir es decir a lo que tengo en el fichero añado.
    
el ciclo de vida de un fichero consta de tres partes:
abrir fichero - realizar las acciones correspondientes W-R-A - cerrar fichero
    
"""

# paso 1: donde esta el fichero. Ruta
mi_fichero = open('./texto.txt', 'r', encoding='UTF-8')

frases = []

# read() me sirve para leer todo el fichero de golpe, pero no lo puedo manejar.
# print(mi_fichero.read())

# readlines() me sirve para crear una lista por cada parrafo del txt
# print( mi_fichero.readlines() )

# vamos a coger linea a linea, limpiamos el texto y lo metemos en la lista de frases
for linea in mi_fichero.readlines():
    linea =linea.replace('\n', "")
    print(linea)
    frases.append(linea)
else:
    print(frases)

# muy importante es al final cerrar el fichero
mi_fichero.close()