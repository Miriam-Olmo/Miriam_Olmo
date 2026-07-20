# ============================================
# LIB/AUDITORIA.PY
# ============================================

valores_vacios = [

    "",

    None,

    "N/A",

    "-",

    "null",

    "no disponible"
]

# ============================================
# CONTAR REGISTROS
# ============================================

def contar_total_registros(
    lista_datos
):

    return len(
        lista_datos
    )

# ============================================
# OBTENER CAMPOS
# ============================================

def obtener_campos(
    lista_datos
):

    if len(lista_datos) == 0:

        return []

    return list(
        lista_datos[0].keys()
    )

# ============================================
# CONTAR VALORES VACÍOS
# ============================================

def contar_valores_vacios_en_campo(

    lista_datos,

    campo
):

    contador = 0

    for fila in lista_datos:

        valor = fila.get(campo)

        if valor in valores_vacios:

            contador += 1

    return contador

# ============================================
# AUDITAR VALORES VACÍOS
# ============================================

def auditar_valores_vacios(
    lista_datos
):

    resultado = {}

    campos = obtener_campos(
        lista_datos
    )

    for campo in campos:

        cantidad = contar_valores_vacios_en_campo(

            lista_datos,

            campo
        )

        resultado[campo] = cantidad

    return resultado

# ============================================
# DETECTAR ESPACIOS EXTRA
# ============================================

def tiene_espacios_extra(
    valor
):

    valor = str(valor)

    return (

        valor != valor.strip()

        or

        "  " in valor
    )

# ============================================
# CONTAR ESPACIOS EXTRA
# ============================================

def contar_espacios_extra_en_campo(

    lista_datos,

    campo
):

    contador = 0

    for fila in lista_datos:

        valor = fila.get(campo, "")

        if tiene_espacios_extra(
            valor
        ):

            contador += 1

    return contador

# ============================================
# AUDITAR ESPACIOS EXTRA
# ============================================

def auditar_espacios_extra(
    lista_datos
):

    resultado = {}

    campos = obtener_campos(
        lista_datos
    )

    for campo in campos:

        cantidad = contar_espacios_extra_en_campo(

            lista_datos,

            campo
        )

        resultado[campo] = cantidad

    return resultado

# ============================================
# CREAR CLAVE DE DUPLICADO
# ============================================

def crear_clave_duplicado(
    fila
):

    return tuple(

        str(valor).lower().strip()

        for valor in fila.values()
    )

# ============================================
# CONTAR DUPLICADOS
# ============================================

def contar_duplicados(
    lista_datos
):

    registros_vistos = set()

    contador_duplicados = 0

    for fila in lista_datos:

        clave = crear_clave_duplicado(
            fila
        )

        if clave in registros_vistos:

            contador_duplicados += 1

        else:

            registros_vistos.add(
                clave
            )

    return contador_duplicados

# ============================================
# MOSTRAR RESULTADOS
# ============================================

def mostrar_resultado_auditoria(

    nombre_archivo,

    auditoria
):

    print("\n========================")

    print(
        f"AUDITORÍA: {nombre_archivo}"
    )

    print("========================")

    print(
        f"Total registros: "
        f"{auditoria['total_registros']}"
    )

    print("\nVALORES VACÍOS:")

    for campo, cantidad in auditoria[
        "valores_vacios"
    ].items():

        print(
            f"{campo}: {cantidad}"
        )

    print("\nESPACIOS EXTRA:")

    for campo, cantidad in auditoria[
        "espacios_extra"
    ].items():

        print(
            f"{campo}: {cantidad}"
        )

    print(
        f"\nDUPLICADOS: "
        f"{auditoria['duplicados']}"
    )

# ============================================
# AUDITORÍA GENERAL
# ============================================

def auditar_datos(
    lista_datos,
    nombre_archivo
):

    auditoria = {}

    auditoria[
        "total_registros"
    ] = contar_total_registros(
        lista_datos
    )

    auditoria[
        "valores_vacios"
    ] = auditar_valores_vacios(
        lista_datos
    )

    auditoria[
        "espacios_extra"
    ] = auditar_espacios_extra(
        lista_datos
    )

    auditoria[
        "duplicados"
    ] = contar_duplicados(
        lista_datos
    )

    mostrar_resultado_auditoria(

        nombre_archivo,

        auditoria
    )

    return auditoria