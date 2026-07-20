# vamos a ver funciones que me permita manipular texto

""" existen un serie de funciones / acciones que me permiten modificar las cadenas de texto

vamos encontrarnos funciones que reciben un texto por parametro

        nombre_funcion(texto)
        len(nombre)

vamos encontrarnos funciones que se aplican al texto
        texto.nombre_funcion()
        nombre.upper()

"""

# funciones que permite convertir texto sin modificar el original

texto = "hOlA"
titulo = "Hola COMO Estas"
# pasar todo a minusculas
print(texto.lower()) # hola
# pasar todo a MAYUSCULAS
print(texto.upper()) # HOLA
# convertir el texto en Capitular Hola
print(titulo.capitalize()) # Hola como estas
# convertir la primera letra de cada palabra en mayuscula
print(titulo.title()) # Hola Como Estas
# i
print(texto.swapcase()) # hOlA => HoLa


# funciones de comprobación

dni = '456789V'
print( dni.zfill(9) )

# metodos de busquedas dentro de la cadena.
frase = "En un lugar de la manchA"

# cantidad de caracteres
print( len(frase) ) # numero de caracteres

# cuantas "a" hay en la cadena
print('numero de as', frase.lower().count('a'))

# replazar un texto por otro, no modifica la variable original
nombre = 'Pablo'
frase = 'David tiene un ferrari'
frase_cambiada = frase.replace('David', nombre)
print(frase_cambiada)

# en esta frase: Como estan los maquinas, quitar los espacios. Comoestanlosmaquinas
texto = "Como estan los maquinas"
texto_final = texto.replace(" ", "", 1)
print(texto_final)

