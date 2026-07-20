# quiero saber si una palabra o frase es un palindromo
# Ana => anA
# un palindromo es una palabra que se lee igual al derecho que al reves sin contar mayusculas ni acentos ni espacios en blanco.

# ejemplos de palindromos
#Anita lava la tina.
#Isaac no ronca así.
#Dábale arroz a la zorra el abad.
#Sé verlas al revés.
#Amo la paloma.
# Ojo, Somos, Reconocer



def quitar_acentos(texto):
    texto = texto.lower()
    texto_limpio = ""
    for caracter in texto:
        if caracter == 'á':
            texto_limpio += 'a'
        elif caracter == 'é':
            texto_limpio += 'e'
        elif caracter == 'í':
            texto_limpio += 'i'
        elif caracter == 'ó':
            texto_limpio += 'o'
        elif caracter == 'ú' or caracter == 'ü':
            texto_limpio += 'u'
        else:
            texto_limpio += caracter
    return texto_limpio

def quitar_espacios(texto):
    texto = texto.replace(' ', '')
    return texto
    
def invertir_texto(texto):
    # opcion 1: recorriendo un un for
    # texto_invertido = ''
    # for caracter in texto:
    #     texto_invertido = caracter + texto_invertido
    # opcion 2: con manejo de posiciones [inicio:fin:paso]
    texto_invertido = texto[::-1]
    return texto_invertido

# paso 1: recibimos un texto como parametro dentro de la funcion ✅
# paso 2: convertir en minusculas ✅
# paso 3: quitar acentos ✅
# paso 4: quitar los espacios ✅
# paso 5: invertir texto ✅


def es_palindromo(texto):
    texto_final = texto.lower()
    texto_final_sin_acentos = quitar_acentos(texto_final)
    text_final_sin_acentos_sin_espacios = quitar_espacios(texto_final_sin_acentos)
    texto_invertido = invertir_texto(text_final_sin_acentos_sin_espacios)
    if text_final_sin_acentos_sin_espacios == texto_invertido:
        print('Es palindromo')
    else:
        print('No es palindromo')
    
    
es_palindromo('Isaac no ronca así')