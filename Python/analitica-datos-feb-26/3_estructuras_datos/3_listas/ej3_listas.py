lista_productos = [('laptop', 1200),('raton', 39),('ram', 200), ('teclado', 10)]
#raton = ('raton', 39)
print(lista_productos[3][0])


lista_ordenada = sorted(lista_productos, key=lambda producto: producto[1], reverse=True)
print(lista_ordenada)

# ordena a los alumnos por altura del mas alto al mas bajo
alumnos = [('Carlos', 34, 180), ('Lucia', 24, 165), ('Raul', 18, 190), ('Berta', 24, 172)]

lista_alumnos_alturas = sorted( alumnos, key=lambda alumno: alumno[2], reverse=True)
print(lista_alumnos_alturas)