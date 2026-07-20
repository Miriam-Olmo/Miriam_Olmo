# python tiene una libreria especial para funciones matemáticas complejas math. Para usarla tenemos que importarla al principio del script
# tiene libreria operaciones matematicas math
# https://docs.python.org/3/library/math.html

import math
from decimal import Decimal

# funciones de conversion
numero = 5
print( float(numero) ) # 5.0 racional
print( int(3.3) ) # 3 integer

# redondeo de un numero
numero = 4.567892
print( round(numero, 4) ) # matematico

# redondeo a la alta
redondeo_alta = math.ceil(numero) #5
print(redondeo_alta)
# redondeo a la baja
print(math.floor(numero)) #4
# raiz cuadrada de un numero
print(math.sqrt(256)) # 16
# suma de un conjunto de numeros
suma_total = math.fsum([1,2,3,4,5,6]) # 21
print(suma_total)


# a modo reto 
nota = 4.999999999999999999999
print(nota)

print(round(nota, 3))
print(math.trunc(nota))

otra_nota = input('Dime tu nota: ')
print(float(otra_nota[0:5]))


