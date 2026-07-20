# -----------------------------------------
# DICCIONARIOS DE SOPORTE Y MAPEO
# -----------------------------------------

correcciones_tildes = {
    "jose": "José", "maria": "María", "garcia": "García", "gonzalez": "González",
    "martinez": "Martínez", "lopez": "López", "perez": "Pérez", "sanchez": "Sánchez",
    "gomez": "Gómez", "fernandez": "Fernández", "rodriguez": "Rodríguez", 
    "hernandez": "Hernández", "ramirez": "Ramírez", "gutierrez": "Gutiérrez"
}

mapeos_categorias = {
    "genero_musical": {
        "rock": "Rock", "rokc": "Rock", "roc": "Rock",
        "electro": "Electrónica", "electronica": "Electrónica", "electrónica": "Electrónica", "electrónic": "Electrónica",
        "hip hop": "Hip Hop", "hip-hop": "Hip Hop", "hiphop": "Hip Hop",
        "jazz": "Jazz", "jaz": "Jazz", "metal": "Metal", "metall": "Metal",
        "pop": "Pop", "ppo": "Pop", "r&b": "R&B", "r & b": "R&B", "rnb": "R&B",
        "reggaeton": "Reggaetón", "regueton": "Reggaetón", "reguetón": "Reggaetón",
        "ska": "Ska", "salsa": "Salsa", "techno": "Techno", "tekno": "Techno",
        "flamenco": "Flamenco", "flamenko": "Flamenco", "folk": "Folk",
        "indie": "Indie", "indy": "Indie", "cumbia": "Cumbia", "kunbia": "Cumbia"
    },
    "pais": {
        "españa": "España", "espana": "España", "spain": "España",
        "usa": "Estados Unidos", "united states": "Estados Unidos", "uk": "Reino Unido"
    },
    "escenario": {
        "escenario principal": "Escenario Principal", "principal": "Escenario Principal",
        "escenario 2": "Escenario Secundario", "secundario": "Escenario Secundario",
        "carpa techno": "Carpa Techno"
    },
    "tipo_entrada": {
        "general": "General", "vip": "VIP", "early bird": "Early Bird", "abono": "Abono Completo"
    },
    "metodo_pago": {
        "tarjeta": "Tarjeta", "credit card": "Tarjeta", "paypal": "PayPal", "efectivo": "Efectivo"
    },
    "categoria": {
        "main sponsor": "Principal", "principal": "Principal", "colaborador": "Colaborador", "partner": "Colaborador"
    }
}

meses_maestros = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
}


# -----------------------------------------
# FUNCIONES DE TEXTO
# -----------------------------------------
def limpiar_texto(texto):
    if texto is None: 
        return ""
    # Dividir por espacios en blanco y volver a juntar (elimina saltos de línea y espacios múltiples)
    return " ".join(str(texto).split()).strip()

def normalizar_texto(texto):
    texto_limpio = limpiar_texto(texto)
    if not texto_limpio: 
        return ""
    
    palabras = texto_limpio.split()
    palabras_procesadas = []
    for palabra in palabras:
        palabra_title = palabra.title()
        palabra_procesada = correcciones_tildes.get(palabra_title.lower(), palabra_title)
        palabras_procesadas.append(palabra_procesada)
        
    return " ".join(palabras_procesadas)


def limpiar_espacios(texto):
    """Elimina espacios en los extremos y colapsa los dobles espacios intermedios."""
    if texto is None:
        return ""
    return " ".join(str(texto).split())


def es_valor_vacio(texto):
    """Determina si una cadena equivale conceptualmente a un dato ausente."""
    texto_limpio = limpiar_espacios(texto).upper()
    valores_nulos = ["", "N/A", "-", "NO DISPONIBLE", "VACIO", "NONE"]
    return texto_limpio in valores_nulos


def corregir_palabra_tilde(palabra):
    """Busca una palabra individual en el diccionario de tildes o aplica mayúscula inicial."""
    palabra_min = palabra.lower().strip()
    if palabra_min in correcciones_tildes:
        return correcciones_tildes[palabra_min]
    
    if len(palabra) > 0:
        return palabra[0].upper() + palabra[1:]
    return palabra



# -----------------------------------------
# FUNCIONES DE NÚMEROS Y MONEDAS
# -----------------------------------------

def limpiar_simbolos_moneda(cadena):
    """Quita los caracteres de divisa y espacios en blanco internos."""
    return cadena.replace('€', '').replace('$', '').replace(' ', '')


def unificar_separadores_decimales(cadena):
    """Transforma formatos numéricos europeos (puntos en miles, comas en decimales) a estándar."""
    if ',' in cadena and '.' in cadena:
        cadena = cadena.replace('.', '')  # Elimina separador de miles
        cadena = cadena.replace(',', '.')  # Convierte decimal
    elif ',' in cadena:
        cadena = cadena.replace(',', '.')
    return cadena


def limpiar_valor_numerico(valor):
    """Transforma de manera segura importes sucios a float."""
    if valor == None or es_valor_vacio(str(valor)):
        return None
    try:
        cadena_limpia = str(valor).strip().lower()
        cadena_limpia = cadena_limpia.replace("€", "").replace("$", "").replace("eur", "")
        cadena_limpia = "".join(cadena_limpia.split())
        
        if "," in cadena_limpia and "." in cadena_limpia:
            if cadena_limpia.find(".") < cadena_limpia.find(","):
                cadena_limpia = cadena_limpia.replace(".", "").replace(",", ".")
            else:
                cadena_limpia = cadena_limpia.replace(",", "")
        elif "," in cadena_limpia:
            partes_decimales = cadena_limpia.split(",")
            if len(partes_decimales[-1]) == 2:
                cadena_limpia = cadena_limpia.replace(",", ".")
            else:
                cadena_limpia = cadena_limpia.replace(",", "")
                
        if "." in cadena_limpia:
            return float(cadena_limpia)
        return int(cadena_limpia)
    except ValueError:
        return None


# -----------------------------------------
# FUNCIONES DE IDENTIFICADORES Y FORMATOS ESPECÍFICOS
# -----------------------------------------

def limpiar_id(identificador):
    """Estandariza códigos de identificación a minúsculas sin espacios."""
    # CORREGIDO: Se cambia 'valor' por 'identificador'
    if identificador is None or es_valor_vacio(str(identificador)):
        return "SIN DATOS"
    return str(identificador).strip().lower()


def limpiar_dni(dni):
    """Aplica el rellenado con ceros a la izquierda y valida la estructura."""
    if dni is None or es_valor_vacio(str(dni)):
        return "SIN DATOS"
    
    dni_limpio = str(dni).strip().upper()
    dni_formateado = dni_limpio.zfill(9)  # Asegura longitud de 9
    
    # Comprobación de estructura 
    parte_num = dni_formateado[:8]
    parte_letra = dni_formateado[-1]
    
    if len(dni_formateado) == 9 and parte_num.isdigit() and parte_letra.isalpha():
        return dni_formateado
    
    print(f"AVISO CRÍTICO: Estructura de DNI corrupta detectada → '{dni}'")
    return "REVISAR MANUALMENTE"


def normalizar_categoria(valor, diccionario_mapeo, campo_nombre="categoria"):
    """Normaliza un campo categórico cruzándolo con su diccionario de mapeo."""
    if valor is None or es_valor_vacio(str(valor)) or valor == "SIN DATOS":
        return "SIN DATOS"
        
    valor_limpio = str(valor).lower().strip()
    
    if valor_limpio in diccionario_mapeo:
        return diccionario_mapeo[valor_limpio]
    
    print(f"AVISO: Valor no reconocido en {campo_nombre} → '{valor}'")
    return valor


# ------------------------------------------
# FUNCIONES DE TRATAMIENTO DE FECHAS 
#------------------------------------------

def formato_texto_largo(cadena):
    """Procesa formato: 'DD de mes de AAAA' (ej. 15 de julio de 2026)."""
    partes = cadena.split(" de ")
    if len(partes) == 3:
        try:
            dia = int(partes[0].strip())
            mes = meses_maestros.get(partes[1].strip().lower())
            anio = int(partes[2].strip())
            return dia, mes, anio
        except ValueError:
            pass
    return None, None, None


def formato_americano(cadena):
    """Procesa formato: 'mes DD, AAAA' (ej. julio 15, 2026)."""
    cadena_limpia = cadena.replace(",", "")
    partes = tuple(cadena_limpia.split())
    if len(partes) == 3:
        try:
            m = meses_maestros.get(partes[0].strip().lower())
            d = int(partes[1].strip())
            a = int(partes[2].strip())
            return d, m, a
        except ValueError:
            pass
    return None, None, None


def formato_guiones(cadena):
    """Procesa formatos basados en guiones: AAAA-MM-DD o DD-MM-AAAA."""
    partes = cadena.split("-")
    if len(partes) == 3:
        try:
            if len(partes[0].strip()) == 4:  # AAAA-MM-DD
                a = int(partes[0].strip())
                m = int(partes[1].strip())
                d = int(partes[2].strip())
            else:  # DD-MM-AAAA o DD-mes-AAAA
                d = int(partes[0].strip())
                centro = partes[1].strip().lower()
                m = int(centro) if centro.isdigit() else meses_maestros.get(centro)
                a = int(partes[2].strip())
            return d, m, a
        except ValueError:
            pass
    return None, None, None


def formato_barras(cadena):
    """Procesa formatos basados en barras: DD/MM/AAAA o DD/M/AA."""
    partes = cadena.split("/")
    if len(partes) == 3:
        try:
            d = int(partes[0].strip())
            m = int(partes[1].strip())
            anio_str = partes[2].strip()
            a = int(anio_str) + 2000 if len(anio_str) == 2 else int(anio_str)
            return d, m, a
        except ValueError:
            pass
    return None, None, None


def normalizar_fecha(fecha_texto):
    """Función unificadora que enruta la cadena hacia su analizador correspondiente.
    
    Construye y devuelve una cadena de texto (un string) que representa una fecha 
    con el formato estandarizado Día/Mes/Año.
    
    El truco de magia: :02d
    Tanto en {dia:02d} como en {mes:02d}, estamos aplicando un formateo especial 
    a los números enteros. Si lo dividimos en tres partes:
      - d: Indica que la variable que hay dentro es un entero (decimal integer).
      - 2: Indica el ancho mínimo que debe tener el texto resultante (2 caracteres).
      - 0: Indica con qué carácter queremos rellenar el espacio vacío (con ceros).
    """
    if fecha_texto is None or es_valor_vacio(str(fecha_texto)):
        return "FECHA INVÁLIDA"
        
    cadena = str(fecha_texto).strip().lower()
    dia, mes, anio = None, None, None

    if " de " in cadena:
        dia, mes, anio = formato_texto_largo(cadena)
    elif "," in cadena:
        dia, mes, anio = formato_americano(cadena)
    elif "-" in cadena:
        dia, mes, anio = formato_guiones(cadena)
    elif "/" in cadena:
        dia, mes, anio = formato_barras(cadena)

    # Validación final del calendario
    if dia is not None and mes is not None and anio is not None:
        if 1 <= dia <= 31 and 1 <= mes <= 12 and anio > 0:
            return f"{dia:02d}/{mes:02d}/{anio}"
            
    print(f"AVISO: Estructura de fecha no reconocida → '{fecha_texto}'")
    return "FECHA INVÁLIDA"


# ------------------------------------------------------------------------------
# FILTRADO E INTEGRIDAD LOGICA
# ------------------------------------------------------------------------------

def contar_vacios(registro):
    """Cuenta cuántos campos vacíos o marcados con alertas tiene un diccionario."""
    alertas_vacio = ["", "SIN DATOS", "FECHA INVÁLIDA", "REVISAR MANUALMENTE", None]
    return sum(1 for valor in registro.values() if valor in alertas_vacio)


def eliminar_duplicados(datos, campos_clave):
    """Elimina duplicados manteniendo el registro que contenga mayor cantidad de información."""
    tabla_unicos = {}
    conteo_eliminados = 0
    
    for registro in datos:
        # Generamos clave única usando los campos asignados
        clave = tuple(str(registro.get(campo, "")).lower().strip() for campo in campos_clave)
        
        vacios_actual = contar_vacios(registro)
        
        if clave in tabla_unicos:
            conteo_eliminados += 1
            vacios_guardado = contar_vacios(tabla_unicos[clave])
            # Si el nuevo registro tiene menos campos vacíos, lo sustituimos
            if vacios_actual < vacios_guardado:
                tabla_unicos[clave] = registro
        else:
            tabla_unicos[clave] = registro
            
    return list(tabla_unicos.values()), conteo_eliminados