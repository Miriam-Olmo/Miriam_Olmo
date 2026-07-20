# una lista es un conjunto de elementos casi siempre del mismo tipo ordenado por posicion
lista_nombres = ['Miguel Angel', 'Pablo', 'Lara', 'Paula']
lista = ['Juan', 44, True]

# Longitud - cantidad de elementos
print( len(lista_nombres) ) # 4

# imprimir un valor de la lista
print( lista_nombres[2] ) # Lara

# añadir elementos a lista por el final
nombre_nuevo = 'Reniel'
lista_nombres.append(nombre_nuevo)
print( lista_nombres )

# recorrer la lista - varios metodos para recorrer una lista.

for i in range(len(lista_nombres)):
    print(lista_nombres[i])
    
    
print('------------------')

for nombre in lista_nombres:
    print(nombre)
    # if nombre == 'Pablo':
       # break
else:
    print('la lista ha terminado')
    
## cambiar cualquier elemento de la lista. Es mutable
lista_nombres[1] = 'Miriam'
print(lista_nombres)
    
