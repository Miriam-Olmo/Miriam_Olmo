    # 1 almacenar la cantidad de unidades
    # 2 pedir esa cantidad por pantalla
    # 3 convertir la unidad en numero
    # 4 meterla en el for
    # 5 ejecutar el script


cantidad = int(input('dime una cantidad: '))
print(type(cantidad))

for i in range(cantidad):
    print(f'¡Hola!!! {i}')


print('-------------------')


# version 2 (poder elegir punto de inicio y punto de fin en el bucle)
valor = 'dime en rango'
for i in range(valor):
    print(f'valor : {i}')

#version 3 poder elegir punto inicio, fin y salto a cuentas

for i in range(2, 15, 3):
    print(f'valor : {i}')