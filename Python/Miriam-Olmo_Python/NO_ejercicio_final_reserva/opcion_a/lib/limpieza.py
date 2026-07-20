# ============================================
# LIB/LIMPIEZA.PY
# ============================================

# ============================================
# CORRECCIONES DE TILDES
# ============================================

correcciones_tildes = {

    "jose": "José",
    "maria": "María",

    "garcia": "García",
    "gonzalez": "González",
    "martinez": "Martínez",

    "lopez": "López",
    "perez": "Pérez",
    "sanchez": "Sánchez",

    "gomez": "Gómez",
    "fernandez": "Fernández",
    "rodriguez": "Rodríguez",

    "hernandez": "Hernández",
    "ramirez": "Ramírez",
    "gutierrez": "Gutiérrez"
}

# ============================================
# MAPEOS DE CATEGORÍAS
# ============================================

mapeos_categorias = {

    "genero_musical": {

        "rock": "Rock",
        "rokc": "Rock",

        "electro": "Electrónica",
        "electronica": "Electrónica",

        "pop": "Pop",

        "hip hop": "Hip Hop",

        "jazz": "Jazz"
    },

    "pais": {

        "espana": "España",
        "españa": "España",
        "spain": "España",

        "usa": "Estados Unidos",

        "uk": "Reino Unido"
    },

    "escenario": {

        "escenario principal": "Escenario Principal",

        "principal": "Escenario Principal",

        "escenario 2": "Escenario Secundario",

        "secundario": "Escenario Secundario",

        "carpa techno": "Carpa Techno"
    },

    "tipo_entrada": {

        "general": "General",

        "vip": "VIP",

        "early bird": "Early Bird",

        "abono": "Abono Completo"
    },

    "metodo_pago": {

        "tarjeta": "Tarjeta",

        "credit card": "Tarjeta",

        "paypal": "PayPal",

        "efectivo": "Efectivo"
    },

    "categoria": {

        "main sponsor": "Principal",

        "principal": "Principal",

        "colaborador": "Colaborador",

        "partner": "Colaborador"
    }
}

# ============================================
# MESES MAESTROS
# ============================================

meses_maestros = {

    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,

    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,

    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,

    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12
}

# ============================================
# FUNCIONES DE TEXTO
# ============================================

def convertir_valor_a_texto(
    valor
):

    if valor is None:

        return ""

    return str(valor)

# ============================================

def eliminar_espacios_inicio_y_final(
    texto
):

    return texto.strip()

# ============================================

def eliminar_espacios_multiples(
    texto
):

    return " ".join(
        texto.split()
    )

# ============================================

def limpiar_texto(
    texto
):

    texto = convertir_valor_a_texto(
        texto
    )

    texto = eliminar_espacios_inicio_y_final(
        texto
    )

    texto = eliminar_espacios_multiples(
        texto
    )

    return texto

# ============================================
# FUNCIONES DE TILDES
# ============================================

def dividir_texto_en_palabras(
    texto
):

    return texto.split()

# ============================================

def unir_palabras_en_texto(
    lista_palabras
):

    return " ".join(
        lista_palabras
    )

# ============================================

def corregir_tilde_de_palabra(
    palabra
):

    palabra_limpia = palabra.lower()

    if palabra_limpia in correcciones_tildes:

        return correcciones_tildes[
            palabra_limpia
        ]

    return palabra.capitalize()

# ============================================

def corregir_tildes_del_texto(
    texto
):

    palabras = dividir_texto_en_palabras(
        texto
    )

    palabras_corregidas = []

    for palabra in palabras:

        palabra_corregida = corregir_tilde_de_palabra(
            palabra
        )

        palabras_corregidas.append(
            palabra_corregida
        )

    return unir_palabras_en_texto(
        palabras_corregidas
    )

# ============================================

def normalizar_texto(
    texto
):

    texto = limpiar_texto(
        texto
    )

    texto = corregir_tildes_del_texto(
        texto
    )

    return texto

# ============================================
# FUNCIONES DE CATEGORÍAS
# ============================================

def convertir_categoria_a_minusculas(
    valor
):

    valor = convertir_valor_a_texto(
        valor
    )

    valor = valor.lower()

    valor = valor.strip()

    return valor

# ============================================

def normalizar_categoria(
    valor,
    tipo_categoria
):

    valor_original = valor

    valor = convertir_categoria_a_minusculas(
        valor
    )

    categorias = mapeos_categorias.get(
        tipo_categoria,
        {}
    )

    if valor in categorias:

        return categorias[valor]

    print(

        f"AVISO: valor no reconocido "

        f"en {tipo_categoria}: {valor_original}"
    )

    return valor_original

# ============================================
# FUNCIONES NUMÉRICAS
# ============================================

def eliminar_simbolos_monetarios(
    valor
):

    valor = valor.replace(
        "€",
        ""
    )

    valor = valor.replace(
        "$",
        ""
    )

    return valor

# ============================================

def eliminar_puntos_de_miles(
    valor
):

    return valor.replace(
        ".",
        ""
    )

# ============================================

def convertir_comas_decimales(
    valor
):

    return valor.replace(
        ",",
        "."
    )

# ============================================

def convertir_texto_a_float(
    valor
):

    return float(valor)

# ============================================

def limpiar_valor_numerico(
    valor
):

    if valor is None:

        return None

    try:

        valor = convertir_valor_a_texto(
            valor
        )

        valor = eliminar_espacios_inicio_y_final(
            valor
        )

        valor = eliminar_simbolos_monetarios(
            valor
        )

        valor = eliminar_puntos_de_miles(
            valor
        )

        valor = convertir_comas_decimales(
            valor
        )

        valor = convertir_texto_a_float(
            valor
        )

        return valor

    except:

        return None

# ============================================
# FUNCIONES DE FECHAS
# ============================================

def normalizar_fecha(
    fecha
):

    if not fecha:

        return "FECHA INVÁLIDA"

    try:

        fecha = convertir_valor_a_texto(
            fecha
        )

        fecha = fecha.lower().strip()

        if "-" in fecha:

            año, mes, dia = fecha.split(
                "-"
            )

        elif "/" in fecha:

            dia, mes, año = fecha.split(
                "/"
            )

        elif " de " in fecha:

            partes = fecha.split(
                " de "
            )

            dia = partes[0]

            mes = meses_maestros[
                partes[1]
            ]

            año = partes[2]

        else:

            return "FECHA INVÁLIDA"

        return (

            f"{int(dia):02d}/"

            f"{int(mes):02d}/"

            f"{int(año)}"
        )

    except:

        return "FECHA INVÁLIDA"

# ============================================
# FUNCIONES DE DUPLICADOS
# ============================================

def crear_clave_unica(
    registro,
    campos_clave
):

    return tuple(

        str(
            registro[campo]
        ).lower().strip()

        for campo in campos_clave
    )

# ============================================

def contar_campos_vacios(
    registro
):

    contador = 0

    for valor in registro.values():

        if not valor:

            contador += 1

    return contador

# ============================================

def eliminar_duplicados(
    lista_datos,
    campos_clave
):

    registros_unicos = {}

    for registro in lista_datos:

        clave = crear_clave_unica(

            registro,

            campos_clave
        )

        if clave not in registros_unicos:

            registros_unicos[
                clave
            ] = registro

        else:

            registro_actual = registros_unicos[
                clave
            ]

            vacios_actual = contar_campos_vacios(
                registro_actual
            )

            vacios_nuevo = contar_campos_vacios(
                registro
            )

            if vacios_nuevo < vacios_actual:

                registros_unicos[
                    clave
                ] = registro

    return list(
        registros_unicos.values()
    )