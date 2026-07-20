valor = input('Dime algo bonito: ')
print( valor.isdigit()) # solo digitos numeros
print( valor.isalpha() ) # solo letras
print( valor.isalnum() ) # numeros y letras.
print( valor.isnumeric() ) # si es numero

## saber si una cadena de caracteres empieza, termina o incluye un determinado caracter. True o False

texto = "En un lugar de la mancha"
print(texto.startswith('e')) # False
print(texto.endswith('a')) # True

# saber si algo esta incluido
busqueda = input('Dime que quieres buscar: ')
resultado = busqueda.lower() in texto.lower()
print('incluido', resultado)