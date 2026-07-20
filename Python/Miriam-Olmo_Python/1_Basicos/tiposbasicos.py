nombre_alumno ="Miriam Olmo"
print(nombre_alumno) # Miriam Olmo
print(type(nombre_alumno))

nombre_alumno =22
print(nombre_alumno)
print(type(nombre_alumno))


# tipos basicos en python
# numericos: almacenan numeros

edad = 36
grados = -15
precio = 199.99


#booleano: solo si/no, verdadero/falso

estado = True
activo = False

# cadena de caracteres - string

nombre = "Irene"
apellidos = " Martinez"
mensaje = 'El niño dijo : "Qué pasa"'
print(mensaje)

# objetivo : Irene Martinez: 36
nombre_completo = nombre + " "+ apellidos + ": " + str(edad)
print(nombre_completo)

nombre_completo2 = f'{nombre} {apellidos}: {edad}'
print(nombre_completo2)

texto_largo = """
selecciona una opción
[1] Sopa
[2] pure de calabaza
[3] Gazpacho
"""

opcion = input(texto_largo)
print(f'la opcion es {opcion}')