# and, or, not
precio = float(input('Dime un precio: '))
marca = input('Dime una marca: ')

resultado = (precio > 100) and (marca == "apple")
print(resultado)

# Número par o divisible por 5
# 1. Pedir el número
# 2. Hacer la comprobación

numero = float(input('Introduce un número: '))
# es_par = numero % 2 == 0
# multiplo_5 = numero % 5 == 0

resultado = numero % 2 == 0 or numero % 5 == 0
print(resultado)

# Negación

esta_activo = True
print(not esta_activo)