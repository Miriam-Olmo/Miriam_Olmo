# una lista es un conjunto de elementos casi siempre el mismo tipo ordenados por posicion
lista_nombres = ['Miguel', 'Pablo', 'Lara', 'David']

# longitud-cantidad de elementos
print( len(lista_nombres) )

# imprimir un valor de la lista
print(lista_nombres[2]) # Lara

# añadir elementos a la lista
nombre_nuevo = 'Reniel'

lista_nombres.append(nombre_nuevo) # solo deja añadir elementos de uno en uno
print(lista_nombres)

# recorrer la lista - varios metodos
# 1-
for i in range(len(lista_nombres)):
    print(lista_nombres[i])

print('--------')

# 2-
for nombre in lista_nombres:
    print(nombre)
else:
    print('la lista ha finalizado')



# cambiar cualquier elemento de la lista. es mutable
lista_nombres[1] = 'Miriam'
print(lista_nombres)

