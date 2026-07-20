numeros = [1,2,4,6,14,45,9,34,3,25]
otra_lista = [0,3,4,5,6,674,87,6]

numeros_pares = []
numeros_impares = []

def obtener_lista_pares(lista):
    lista_resultante = []
    for numero in numeros:
        if numero % 2 == 0_:
            lista_resultante.append(numero)
    return lista_resultante

numeros_pares = obtener_lista_pares(otra_lista)
print(numeros_pares)