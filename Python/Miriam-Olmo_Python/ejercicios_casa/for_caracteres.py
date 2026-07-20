# ejercicio 1: Contar vocales en una frase 
# Enunciado: Escribe un programa que pida al usuario una frase y utilice un bucle for para contar cuántas vocales (a, e, i, o, u) tiene. 

frase = input('escribe una frase: ')

print(len(frase))

for i in range(len(frase)):
    print(frase[i])

# Ejercicio 2: Invertir una cadena de texto
# Enunciado: Escribe un programa que tome una palabra ingresada por el usuario y utilice un bucle for para mostrarla al revés. 

palabra = input('escribe una palabra: ')
palabra_invertida = ""

# Iteramos sobre cada carácter directamente
for letra in palabra:
    # Añadimos la letra actual AL PRINCIPIO de la nueva cadena
    palabra_invertida = letra + palabra_invertida

print(f'la palabra es: {palabra}')
print(f'al reves es : {palabra_invertida}')