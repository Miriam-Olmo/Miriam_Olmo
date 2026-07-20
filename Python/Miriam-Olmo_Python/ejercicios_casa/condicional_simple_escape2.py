# Ejercicio 1: Verificador de Mayoría de Edad 
# Escribe un programa que solicite la edad del usuario y determine si es mayor de edad (
#  años) o no. 

edad = int(input('dime tu edad: '))

if edad >= 18:
    print('mayor de edad')
else:
    print('menor de edad')



# Ejercicio 2: Par o Impar 
# Solicita un número entero al usuario y determina si es par o impar utilizando el operador de módulo %.

numero = int(input('dime un numero: ')) 

if numero % 2 == 0:
    print(f'{numero} es par')
else:
    print(f'{numero} es impar')