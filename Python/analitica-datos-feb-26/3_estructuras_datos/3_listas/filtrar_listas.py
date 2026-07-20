### Filtrado de listas.


numeros = [1,2,4,6,74,3,45,7,89,3,34,56,4,53,2,5]
otro_lista = [1,3,4,3,6,674,32,6]

numeros_pares = []
numeros_impares = []


def obtener_lista_pares(lista):
    lista_resultante = []
    for numero in lista:
        if numero % 2 == 0:
            lista_resultante.append(numero)
    return lista_resultante

numeros_pares = obtener_lista_pares(otro_lista)
print(numeros_pares)