# métodos de unión
nombre = "Juan Antonio"
apellido = "Pérez"
edad = 44
separador = " - "

texto = f"{nombre}{separador}{apellido}{separador}{edad}"

otro_texto = separador.join([nombre, apellido, str(edad)])
print(texto)
print(otro_texto)

# metodos de separacion
frase = "El presidente dijo: Hola como estan los maquinas"
resultado = frase.partition(": ")
print(resultado)

# split()
texto = "Porque la vida puede ser maravillosa"
resultado = texto.split(' ')
## crear un conjunto de elementos sin el espacio en blanco
print(resultado[5])

# splitlines() me permite separa lineas en un texto multilinea

cadena = """Hola
bienvenido
al
maravilloso
mundo
python
"""

print(cadena)
conjunto_lineas = cadena.splitlines()
print(conjunto_lineas)

# deletrear un cadena texto cualquier
palabra = "supercalifragilistico"
print(list(palabra))