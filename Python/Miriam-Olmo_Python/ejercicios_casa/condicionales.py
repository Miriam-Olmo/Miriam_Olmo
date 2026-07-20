# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input('que edad tienes: '))

if edad >= 18:
    print('eres mayor de edad')
else:
    print('eres menor de edad')


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "contraseña"
contraseña = input("Introduce la contraseña: ")
if key == contraseña.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

numero1 = float(input(' dime un numero: '))
numero2 = float(input(' dime otro numero: '))

resultado = numero1 / numero2

if numero2 == 0:
    print('error, dividendo no puede ser 0')
else:
    print(float(resultado))