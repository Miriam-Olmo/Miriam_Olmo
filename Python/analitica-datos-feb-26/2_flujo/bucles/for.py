# paso 1: almacenar la cantidad de unidades
# paso 2: pedir esa cantidad por pantalla
# paso 3: convertir la unidad en numero
# paso 4: meterla en for
# paso 5: ejecutar el script

cantidad = int(input('Dime un cantidad: '))
#print( type(cantidad))

for i in range(cantidad):
    print(f'Hola {i}')
    
print('----------------')

# version 2: poder elegir punto de inicio y punto de fin en bucle

for i in range(2, 8):
    print(f"Valor: {i}")
    
print('--------------')

# version 3: poder elegir punto inicio el punto fin y los saltos o cuentas.

for i in range(2, 15, 3):
    print(f'Valor: {i}')
    
