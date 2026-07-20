# Ejercicio: Tabla de Multiplicar
# Pide al usuario un número entero.
# Usa un bucle for para multiplicar ese número del 1 al 10.
# Imprime el resultado en el formato: número x i = resultado. 

numero = int(input('dime un numero: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x{i} = {resultado}')