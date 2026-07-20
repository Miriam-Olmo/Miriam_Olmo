# Realizar una funcion que introduzca el nombre de una persona y me devuelve solo sus iniciales
# ej: Juan Antonio Perez -> "J.A.P."

# paso 1: la primera letra del nombre simpre es la primera inicial
# paso 2: recorrer la cadena de caracteres
# paso 3: buscar lo que separa cada nombre y apellido el espacio
# paso 4: la letra justo despues del espacio es la inicial a convertir

# explicacion previa
#nombre = "Ana Martinez Lopez" # A.M
# print(nombre[0]) # A

def obtener_iniciales(nombre):
    resultado = ""
    for i in range(len(nombre)):
        if i == 0:
            resultado += nombre[i].upper() + "."
        if nombre[i] == " ":
            resultado += nombre[i+1].upper() + "."
    print(resultado)

obtener_iniciales('Juan Antonio Perez Jarillo')
