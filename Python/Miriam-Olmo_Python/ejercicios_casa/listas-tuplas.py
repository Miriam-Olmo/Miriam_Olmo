# Ejercicio 1
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


materias = ['Matematicas', 'lenguaje', 'historia', 'quimica', 'fisica', 'arte']

print(materias)


# Ejercicio 2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

for materia in materias:
    print('yo estudio ' + materia)



# Ejercicio 3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

asignaturas = ['física', 'química', 'lenguaje', 'arte', 'biología']
notas = []

# Pedimos las notas
for asignatura in asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    notas.append(nota)

# Mostramos los resultados iterando por ambas listas
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")



