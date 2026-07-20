# un set es un conjunto ordenado de elementos UNICOS. Se utiliza para eliminar elementos duplicados de un conjunto

# esto es una lista no un set
lista = [1,1,1,2,2,2,2,3,3,3,4,4,5,5,5,5,5,5,3,6,7,5,9]
mi_set = set(lista)
print('lista original', lista)
print('------------')
#print('conjunto_final', mi_set)
print('lista_no_duplicados', list(mi_set))

# conjunto de elementos o set el orden es aleatorio, esto complica un poco el manejo por posicion
frutas = {'Manzana', 'Naranja', 'Pera', 'Platano', 'Pera'}
print(frutas)

# agregar elementos al set
frutas.add('Melón')
frutas.add('Pera') # si el elemento existe no lo añade pero no da error
print(frutas)

# borrar elementos de un set si estamos seguros de su existencia
frutas.remove('Melón')
print(frutas)

# borrar elementos sin saber si existe, si no existe no da error
frutas.discard('sandia')
print(frutas)

# vaciarlo y eliminarlo
frutas.clear()
print(frutas)
del(frutas) # Eliminaria