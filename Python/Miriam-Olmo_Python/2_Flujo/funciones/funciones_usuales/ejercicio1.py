# =============================================================================
# EJERCICIO 1: PROCESADOR DE FRASES
# Pide al usuario una frase.
# Muestra:
#   - La frase con todas las palabras invertidas individualmente
#     (ej: "hola mundo" → "aloh odnum") ✅
#   - devolver la cantidad de letras de la frase ✅
#   - El número de veces que aparece cada vocal (a, e, i, o, u) ✅
#   - La frase con los espacios reemplazados por guiones bajos ✅
#   - La frase con palabras invertidas Tony Stark => Stark Tony ✅
# =============================================================================

def cantidad_letras(frase):
    contador = 0
    for caracter in frase:
        if caracter.isalpha():
            contador += 1
    return contador

texto = input('Dime algo bonito: ')
print(cantidad_letras(texto))


def contar_vocal(frase, vocal):
    return frase.count(vocal)

for vocal in "aeiouáéíóúÁÉÍÓÚAEIOU":
    numero = contar_vocal(texto, vocal)
    if numero != 0:
        print(vocal, numero)
    
    
def frase_con_separador(frase, separador):
    return frase.replace( " ", separador )

print(frase_con_separador(texto, '_'))


## El avión despegó de la pista
## pista la de despegó avión El

# paso 1: convertir en una lista mi frase
# opcion 1: sin funcion
lista_palabras = texto.split(" ")
cantidad = len(lista_palabras)
frase_invertida = ""
while(cantidad > 0):
    frase_invertida += f"{lista_palabras[cantidad-1]} "
    cantidad -= 1
    
print(frase_invertida)

lista_caracteres = list(texto)
cantidad2 = len(list(texto))
frase_invertida2 = ""
while(cantidad2 > 0):
    frase_invertida2 += f"{lista_caracteres[cantidad2 - 1]}"
    cantidad2 -= 1
    
print( frase_invertida2 )


#opcion 2: con funcion 
def invertir_lista(lista, separador):
    cantidad = len(lista)
    frase_invertida = ""
    while(cantidad > 0):
        frase_invertida += f"{lista[cantidad-1]}" + separador
        cantidad -= 1
    print(frase_invertida)

lista_palabras = texto.split(" ")
invertir_lista(lista_palabras , " ")


lista_caracteres = list(texto)
invertir_lista(lista_caracteres, "")
