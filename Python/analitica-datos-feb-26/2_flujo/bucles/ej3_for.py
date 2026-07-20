# quiero pedir un texto por pantalla de cualquier longitud y quiero que pidais un vocal
# contar cuantas vocales tiene el texto.

# paso 1: Pedir el texto por pantalla
texto = input('Dame una frase maravillosa: ').lower()
# paso 2: Pedir una vocal
vocal = input('Dame una vocal: ').lower()

cantidad = len(texto)
# paso 3: pintar todos los caracteres del texto
# paso 4: imprimir solo la vocal pedida
# paso 5: contar las vocales. crear un variable que incremente en 1 cada vez que encuentre mi vocal
numero_vocales = 0
# paula  - a
for i in range(cantidad):
    if texto[i] == vocal:
        numero_vocales = numero_vocales + 1 
        # numero_vocales += 1
print(numero_vocales)