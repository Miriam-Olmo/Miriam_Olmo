def limpiar_texto(texto):
    # elimina espacios al principio y final
    texto = texto.strip()
    # elimina espacios multiples
    while "  " in texto:
        texto = texto.replace("  ", " ")
    # texto limpio sin cambiar mayusculas/minusculas
    return texto


def normalizar_texto(texto):
    # aplica limpiar texto
    texto = limpiar_texto(texto)
    # convierte el texto primera en mayuscula y lo demas en minuscula
    texto = texto.title()
    # corrije tildes que faltan usando el diccionario de correcciones que se proporciona más abajo
    correcciones_tildes = {
    "jose":       "José",      "maria":      "María",
    "garcia":     "García",    "gonzalez":   "González",
    "martinez":   "Martínez",  "lopez":      "López",
    "perez":      "Pérez",     "sanchez":    "Sánchez",
    "gomez":      "Gómez",     "fernandez":  "Fernández",
    "rodriguez":  "Rodríguez", "hernandez":  "Hernández",
    "ramirez":    "Ramírez",   "gutierrez":  "Gutiérrez",
    }
    palabras = texto.split()   # separa el texto en palabras

    for i in range(len(palabras)):
        if palabras[i] in correcciones_tildes:
            palabras[i] = correcciones_tildes[palabras[i]]

    texto = " ".join(palabras)   # vuelve a unir todo

    return texto


# --- Limpiar todos los campos de texto de una lista ---
def limpiar_registros(lista):
    for registro in lista:
        for clave in registro:
            if type(registro[clave]) == str:
                registro[clave] = normalizar_texto(registro[clave])
    return lista