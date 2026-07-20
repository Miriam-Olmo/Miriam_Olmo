animales = ['perro','gato', 'periquito', 'tortuga', 'conejo']

animales2 = animales


# para no hacer un paso por referencia tenemos que generar un copia de la lista original

# metodo 1: copy()

animales3 = animales.copy()

animales[1] = 'nilo'

print(animales)
print(animales2)
print(animales3)


# metodo 2: indices [:]

frutas = ['manzana', 'platano', 'pera', 'sandia']

# un paso por referencia si modifico frutas también modifico frutas2
frutas2 = frutas

# romper la referencia
frutas3 = frutas[:]

frutas[2] = 'naranjas'

print(frutas)
print(frutas2)
print(frutas3)










