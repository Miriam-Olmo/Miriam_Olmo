# Ejercicio 1: Determinar mayoría de edad 
# Escribe un programa que, dada una edad, imprima "Mayor de edad" o "Menor de edad" utilizando una expresión condicional abreviada. 

edad = int(input('dime una edad: '))

mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(mensaje)

# Ejercicio 2: Calcular el número mayor
# Escribe un programa que compare dos números (a y b) y asigne a una variable maximo el valor del número más grande usando el condicional abreviado.

numeroA = int(input('dime el numero A: '))
numeroB = int(input('dime el numero B: '))

maximo = numeroA if numeroA > numeroB else numeroB

print(f"el mayor es {maximo}")