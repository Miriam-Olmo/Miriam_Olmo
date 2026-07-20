# Un set es un conjunto ordenado de elementos unicos. Se utiliza para eliminar elementos duplicados de un conjunto.

#  esto es una lista
lista = [1,1,1,2,2,2,2,3,3,3,4,4,5,5,5,5,5,5,3,6,7,5,9]
mi_set = set(lista)
print('lista_original', lista)
print('------------')
print('conjunto_final', mi_set)
print('--------')
# convertir un set en lista
print('lista_final', list(mi_set))

# u¡conjunto de elementtos o set el orden es aleatorio, esto complica un poco el manejo por posicion
print('-----------')

frutas = {'Manzana', 'Naranja', 'Pera', 'Platano'}
print(frutas)

# agregar elementos al set
frutas.add('Mango')
frutas.add('Pera') # si el elemento existe no lo añade pero no da error
print(frutas)

# borrar elementos del set si estamos seguros de su existencia.

frutas.remove('Mango') 
print(frutas)

# borrar elementos sin saber si existe, si no existe no da error
frutas.discard('Pera') 
frutas.remove('Melon') 
print(frutas)


# vaciarlo 
frutas.clear()
print(frutas)
# eliminarlo
del(frutas) # Eliminaria