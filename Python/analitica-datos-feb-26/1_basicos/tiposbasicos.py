nombre_alumno = "Mario Girón"
print(nombre_alumno) # Mario Girón
print(type(nombre_alumno))

nombre_alumno = 21
print(nombre_alumno)
print(type(nombre_alumno))

# Tipos Básicos en Python

# Numéricos

edad = 36
grados = -27
precio = 1299.35

# booleano

estado = True
activo = False

# cadena de caracteres - string

nombre = "Irene"
apellidos = 'Martínez'
mensaje = 'El niño dijo: "Qué pasa"'
print(mensaje)

# Irene Martínez: 36
nombre_completo = nombre + " " + apellidos + ": " + str(edad)
print(nombre_completo)

nombre_completo2 = f'{nombre} {apellidos}: {edad}'
print(nombre_completo2)

texto_largo = """
Selecciona una opción
[1] Sopa
[2] Puré de calabaza
[3] Gazpacho

"""

opcion = input(texto_largo)
print(f'La opción es {opcion}')