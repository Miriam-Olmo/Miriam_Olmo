# una tupla es un conjunto de datos inmutable (no se puede cambiar, ni el valor ni la longitud) su objetivo es proteger los datos qwue hay dentro- se pueden recorrer de derecha(negativos) a izquierda y de izquierda a derecha(positivos)



mi_primera_tupla = ('Miriam', 33, True)
frutas = ('naranja', 'pera', 'platano', 'melon')
config_db = ('127.0.0.1', 'root', '123456')


print(mi_primera_tupla)
print(frutas)

# como saber la longitud de una tupla

print(len(frutas)) # 4

# como sacar un elemento concreto, un conjunto se enumera de 0 a n-1 siendo n la longitud

print(frutas[2])

print(mi_primera_tupla[0])

print(frutas[-2])

# copiar tupla

otras_frutas = frutas[1:3]
print(otras_frutas)

print(frutas[0:3:2]) # naranja, platano

# uso tipico en el return de las funciones

def devolver_datos_usuario():
    nombre = input('dime un nombre: ')
    edad = input('dime tu edad: ')
    email = input('dime tu email: ')
    return nombre, edad, email
# print(devolver_datos_usuario()[1] )

# recorrer una tupla

for i in range(0, len(frutas)):
    print(frutas[i])

print('----------')

# para recoger elemento por elemento

for fruta in frutas:
    print(fruta)


# el error con las tuplas
"""
frutas[0] = "mandarina" 
"""

# eliminar una tupla

del otras_frutas
print(otras_frutas)

# si creo una tupla de un unico elemento
tupla_unico_elemento = ('Juan') # sin coma lo convierte en cadena de caraceteres; si le pones una coma si aparece como tupla
print(tupla_unico_elemento)