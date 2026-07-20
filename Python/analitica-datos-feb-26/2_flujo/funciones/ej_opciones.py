## Hacer un programa en python que permita elegir entre 5 opciones
        # 1 - pasar un texto a minuscula
        # 2 - contar la cantidad de letras de un texto
        # 3 - invertir el texto => tony stark => stark tony
        # 4 - quitar espacios en blanco del texto y acentos.
        # 5 - salir 
# cualquier opcion no descrita vuelve a ejecutar el programa
def quitar_espacios_acentos(texto):
    texto = texto.replace(" ", "")
    texto = texto.replace("á", 'a')
    texto = texto.replace("é", 'e')
    texto = texto.replace("í", 'i')
    texto = texto.replace("ó", 'o')
    texto = texto.replace("ú", 'u')
    texto = texto.replace("ü", 'u')
    return texto
    
def contar_letras(texto):
    texto = texto.lower()
    # quitar el caracter espacio para que no me lo cuente
    resultado = quitar_espacios_acentos(texto)
    contador = 0
    for caracter in resultado:
        if caracter.isalpha():
            contador += 1
    return f"La cantidad de letras es {contador}"

def invertir_palabras(texto):
    # es convertir en una lista texto
    lista = texto.split(" ")
    texto_invertido = ''
    for palabra in lista:
        texto_invertido = palabra + " " + texto_invertido
    return texto_invertido

def main():
    menu = """
### Bienvenido a nuestra app ###
[1]. Pasar a minúsculas
[2]. Contar caracter o letras
[3]. Invertir el texto introducido
[4]. Quitar espacio en blanco
[x]. Salir    
    """
    print(menu)
    option = input('¿Qué opción quieres hacer? ')
    texto = input('Introduce el texto a transformar: ')
    resultado = ""
    if option == '1':
       resultado = texto.lower()
    elif option == '2':
        resultado = contar_letras(texto)
    elif option == '3':
        resultado = invertir_palabras(texto) 
    elif option == '4':
        resultado = quitar_espacios_acentos(texto)
    elif option == 'x':
        print('Hasta pronto')
    else:
        print('opcion no valida, intentalo de nuevo')
        main()
    print(resultado)

main()