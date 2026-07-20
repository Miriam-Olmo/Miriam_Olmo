# realizar una funcion que me permita evaluar si un numero introducido por parametro es par o impar.si le introducimos el numero 0 tiene que decirme que es el numero 0.

# Definir la función: Usa la palabra clave def y asígnale un nombre descriptivo (por ejemplo, evaluar_numero), asegurándote de que reciba un parámetro.
# Evaluar el caso especial: La primera validación dentro de la función debe ser para el número 0, utilizando una estructura if. #Comprobar la paridad: Si no es cero, utiliza el operador residuo o módulo (%).
    #   Tip técnico: En programación, si un número $n \pmod 2 = 0$, el número es par.
# Manejar los resultados: Utiliza las cláusulas elif y else para diferenciar entre el caso "par" y el "impar".
# Devolver o mostrar el mensaje: Decide si la función debe usar print() para mostrar el resultado directamente o return para devolver el texto.

numero = int(input('dime un numero: '))

def numero_evaluado(numero):
    if numero == 0:
        print('es el numero 0')
    elif numero % 2 == 0:
        print('par')
    elif numero % 2 != 0:
        print('impar')
    else:
        print('no es valido')

numero_evaluado(numero)



# Realizar una funcion que me introduzca un texto y me cuente sus vocales.

# Definir la función: Crea la función (por ejemplo, contar_vocales) que acepte un parámetro de tipo texto.

# Preparar las vocales: Define una variable (string o lista) que contenga las cinco vocales aeiou.

# Inicializar un contador: Crea una variable numérica (por ejemplo, total = 0) para llevar la cuenta.

# Normalizar el texto: Utiliza el método .lower() sobre el texto recibido para que la función detecte tanto "A" como "a".

# Recorrer la cadena: Usa un bucle for para analizar el texto letra por letra.

# Verificar pertenencia: Dentro del bucle, usa un condicional if para saber si la letra actual está en tu variable de vocales (el operador in es ideal aquí).

# Actualizar el total: Si la condición se cumple, suma 1 a tu contador.

# Retornar el valor: Una vez terminado el bucle, devuelve el valor final del contador con return.

vocales = "a", "e", "i", "o", "u"

texto = input('introduce texto: ').lower()

def contador_vocales(texto):
    contador = 0
    for i in range(len(texto)):
        if texto[i] == "a":
            contador += 1
        elif texto[i] == "e":
            contador += 1
        elif texto[i] == "i":
            contador += 1
        elif texto[i] == "o":
            contador += 1
        elif texto[i] == "u":
            contador += 1
    print(contador)



contador_vocales(texto)

# profesor

def contar_vocales(texto):
    contador = 0
    texto = texto.lower()
    for i in range(len(texto)):
        if texto[i] in "aáeéiíoóuú":
         contador += 1

    print('numero_vocales', contador)
contar_vocales(texto)



