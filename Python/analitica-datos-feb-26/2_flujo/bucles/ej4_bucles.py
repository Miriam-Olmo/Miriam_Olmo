# necesito que pidais varios numeros por pantalla y que los sumeis. El programa termina cuando metemos el numero 0;
# while.
# paso 1: pedir numero constantemente
# paso 2: crear una variables suma = 0
# paso 3: añadir a suma el valor introducido previmente convertido.
# paso 4: pulsando 0 acabamos el ejercicio.

print('#' * 40)
print('EJERCICIO 4 - SUMA ACUMULADA')
print('#' * 40)
print(" ")
suma = 0
while True:
    numero = int(input('Introduce un numero: '))
    if numero == 0:
        break
    suma += numero
    
print(suma)
