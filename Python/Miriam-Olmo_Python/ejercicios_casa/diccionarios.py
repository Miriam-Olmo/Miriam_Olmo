# Ejercicio 1
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

moneda = input('dime una moneda: ')
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print('moneda introducida no está registrada')

# Ejercicio 2
# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.


nombre = input('dime tu nombre: ')
edad = input('dime tu edad: ')
direccion = input('dime tu direccion: ')
telefono = input('dime tu numero de telefono: ')
persona = {'nombre': nombre, 'edad':  edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])