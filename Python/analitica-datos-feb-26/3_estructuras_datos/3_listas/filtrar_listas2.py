### Filtrado de listas.


numeros = [1,2,4,6,74,3,45,7,89,3,34,56,4,53,2,5]
otro_lista = [1,3,4,3,6,674,32,6]

numeros_pares = []
numeros_impares = []

# opcion 1: tuplas
"""
def obtener_listas(lista, tipo):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares
    

numeros_pares = obtener_listas(numeros)[0]
numeros_impares = obtener_listas(numeros)[1]
print(numeros_pares)
print(numeros_impares)     
    
"""

# opcion 2: parametros
def obtener_listas(lista, tipo):
    pares = []
    impares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares if tipo == 'pares' else impares
    

numeros_pares = obtener_listas(numeros, 'pares')
numeros_impares = obtener_listas(numeros, 'impares')
print(numeros_pares)
print(numeros_impares)