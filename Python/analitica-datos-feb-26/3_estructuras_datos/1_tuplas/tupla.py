# Una tupla es un conjunto de datos inmutable (no se puede cambiar, ni valor ni de longitud). Proteger los datos que hay dentro.

mi_primera_tupla = ('Juan', 44, True)
frutas = ('naranja', 'pera', 'platano', 'manzana')
config_db = ('127.0.0.1', 'root', '123456')

print(mi_primera_tupla)
print(frutas)

# como saber la longitud tupla
print(len(frutas)) # 4

# como sacar un elemento concreto - un cojunto se numera de 0 a n-1 siendo n lo longtud.
print(frutas[2]) # platano
print(mi_primera_tupla[0]) # Juan
print(frutas[-2]) # platano

una_fruta = frutas[0] # naranja

# copiar una tupla
otras_frutas = frutas[1:3]
print(otras_frutas)

print(frutas[0:3:2]) # naranja, platano


def devolver_datos_usuario():
    nombre = input('Dime un nombre: ')
    edad = int(input('Dime tu edad: '))
    email = input('Dime tu email: ')
    return nombre, edad, email

#print( devolver_datos_usuario()[2] )

print('---------------')

for i in range(0, len(frutas)):
    print(frutas[i])

print('-------------')

for fruta in frutas:
    print(fruta)


# ERROR con tuplas
#frutas[0] = "Mandarina"

#eliminar un tupla
del frutas
#print(frutas)


# si creo una tupla de un único elemento 
tupla_unico_elemento = ('Juan',)
print(tupla_unico_elemento)