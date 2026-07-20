# Realizar una funcion que me permita evaluar si un numero introducido por parametro es par o impar

def evaluar_paridad(numero):
    numero = int(numero)
    if numero == 0:
        print('el numero es 0')
    elif numero % 2 == 0:
        print('es un numero par')
    elif numero % 2 != 0:
        print('es un numero impar')
            
evaluar_paridad('3')

# Realizar una funcion que me introduzca un texto y me cuente sus vocales.

# paso 1: crear la funcion
# paso 2: recoger el texto y pasarlo a minusculas, asi solo tenemos que buscar vocales en minusculas
# paso 3: crear un contador que cuenta vocales inicializado en 0
# paso 4: recorrer toda la cadena de caracteres
# paso 5: exponer todas las condiciones para cada vocal.
# paso 6: pintar el resultado.

def contar_vocales(texto):
    # inicio el contador de vocales
    numero_vocales = 0
    # paso a minusculas el texto
    texto = texto.lower()
    # recorro todo el texto en minuscula
    for i in range(len(texto)):
        if texto[i] in "aeiouáéíóú":
            numero_vocales += 1
    print('numero de vocales', numero_vocales)
    
contar_vocales('En un lugar de la mancha')

    
    





