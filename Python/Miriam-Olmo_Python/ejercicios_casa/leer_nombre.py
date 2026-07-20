nombre = input('dime un nombre: ').lower()
print(nombre)

for caracter in(nombre):
    caracter = len(nombre) # leer caracteres

print(caracter)

for i in range(len(nombre)): #poner caracteres uno por uno
    if nombre[i] == nombre[i].lower():
        print(nombre[i])
