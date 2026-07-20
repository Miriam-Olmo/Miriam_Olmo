# modificar el ejercicio anterior para que admita numeros negativos

lista_numeros = []

while True: # bucle infinito
    numero = input('dime un numero: ')
    numero_sin_negativo = numero.replace("-", "") 
    if not numero_sin_negativo.isdigit():
        break
    lista_numeros.append(int(numero))

print(lista_numeros)