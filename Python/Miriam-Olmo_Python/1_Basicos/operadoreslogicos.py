# and, or, not
#and

precio = float(input('dime un precio: '))
marca = input('dime una marca: ')

Resultado =(precio > 100) and (marca == "SWAROSKY")
print(Resultado)

# or

# numero par o divisible por 5
#1. pedir el numero
#2. hacer comprobacion

numero = float(input('introduce un numero: '))
# es_par = numero % 2 == 0
# multiplo_5 = numero % 5 == 0

resultado = (numero % 2 == 0) or (numero % 5 == 0)

print(resultado)

# not
# nos devuelve el valor contrario

#negacion

esta_activo = True
print(not esta_activo)