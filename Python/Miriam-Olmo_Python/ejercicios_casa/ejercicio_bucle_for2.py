# Ejercicio 1: Tabla de multiplicar
# Escribir un programa que pida al usuario un número entero y muestre por pantalla su tabla de multiplicar del 1 al 10. 

numero = int(input('dime un numero: '))

for i in range(1, 11):
    resultado = numero * i

    print(f'{numero} x {i} = {resultado}')

# Ejercicio 2: Sumar números pares en un rango 
# Escribir un programa que sume todos los números pares que hay entre 1 y un número ingresado por el usuario. 

limite = int(input('dime el numero limite: '))
suma_pares = 0

for i in range(1, limite + 1):
    if i % 2 == 0:
        suma_pares += i

print(f'la suma de los numeros pares hasta {limite} = {suma_pares}')