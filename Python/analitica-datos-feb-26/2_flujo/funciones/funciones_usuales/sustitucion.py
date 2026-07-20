# replace => Sanitizar texto - limpiar textos
frase = 'Ho)laÇm^u)nd^oÇde)sdeÇp)yth^on'
frase = frase.replace(')', '').replace('^','')
frase = frase.replace('Ç', ' ')
print(frase)

otra_frase = "Él envió más café frío allá después según él también pidió algún té allí recién así él podría reír todavía."

def quitar_acentos(texto):
    return texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')

resultado = quitar_acentos(otra_frase)
print(resultado)


# eliminar los espacio en blanco dentro de una palabra. espacio por delante y por detras de la palabra strip(), lstrip(), rstrip()
nombre = "     Juan Antonio      "
print(f'Hola {nombre.strip()} como estas')