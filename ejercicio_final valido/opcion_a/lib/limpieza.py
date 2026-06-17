

# ------------------------------------------------------------------------------
# DICCIONARIOS DE SOPORTE Y MAPEO MAESTRO
# ------------------------------------------------------------------------------

# Estructura de diccionario para mapear variantes lingüísticas, errores ortográficos 
# o siglas de países en nombres oficiales estandarizados (Nomenclatura homogénea).
mapeo_paises = {
    # Bloque de equivalencias para normalizar referencias a España
    "españa": "España",
    "espana": "España",

    # Bloque de equivalencias para normalizar referencias a México (resuelve la jota y el acento)
    "méxico": "México",
    "mexico": "México",
    "mejico": "México",

    # Bloque de equivalencias para normalizar referencias a Argentina (resuelve erratas de tipeo)
    "argentina": "Argentina",
    "argetina": "Argentina",

    # Bloque de equivalencias para normalizar referencias a Brasil (resuelve la traducción al inglés)
    "brasil": "Brasil",
    "brazil": "Brasil",

    # Registro único para el país Chile
    "chile": "Chile",

    # Bloque de equivalencias para normalizar referencias a Colombia (resuelve la errata con 'k')
    "colombia": "Colombia",
    "kolombia": "Colombia",

    # Registro único para el país Cuba
    "cuba": "Cuba",

    # Registro único para el país Italia
    "italia": "Italia",

    # Bloque de equivalencias para normalizar referencias a Francia (resuelve traducción al inglés)
    "francia": "Francia",
    "france": "Francia",

    # Registro único para el país Portugal
    "portugal": "Portugal",

    # Bloque de equivalencias para normalizar referencias a Perú (resuelve la omisión de la tilde)
    "perú": "Perú",
    "peru": "Perú",

    # Registro único para el país Venezuela
    "venezuela": "Venezuela",

    # Bloque de equivalencias para normalizar República Dominicana (resuelve abreviaturas y puntos)
    "r. dominicana": "República Dominicana",
    "rep. dominicana": "República Dominicana",
    "republica dominicana": "República Dominicana",
    "rd": "República Dominicana",

    # Bloque de equivalencias para normalizar Reino Unido (resuelve traducciones, siglas y puntos)
    "reino unido": "Reino Unido",
    "r. unido": "Reino Unido",
    "united kingdom": "Reino Unido",
    "uk": "Reino Unido",

    # Bloque de equivalencias para normalizar Estados Unidos (resuelve abreviaturas y siglas internacionales)
    "estados unidos": "Estados Unidos",
    "ee.uu.": "Estados Unidos",
    "us": "Estados Unidos",
    "usa": "Estados Unidos"
}

# Tabla de sustitución para incorporar tildes obligatorias en nombres y apellidos comunes 
# cuando se procesa texto en minúsculas, garantizando el rigor formal en la entrega.
correcciones_tildes = {
    "jose": "José", "maria": "María", "garcia": "García", "gonzalez": "González",
    "martinez": "Martínez", "lopez": "López", "perez": "Pérez", "sanchez": "Sánchez",
    "gomez": "Gómez", "fernandez": "Fernández", "rodriguez": "Rodríguez", 
    "hernandez": "Hernández", "ramirez": "Ramírez", "gutierrez": "Gutiérrez"
}

# Registro maestro para homogeneizar los nombres de los estilos musicales en el festival
mapeo_genero_musical = {
    # Equivalencias de escritura para el género Rock
    "rock": "Rock", "rokc": "Rock", "roc": "Rock",
    # Agrupación de variantes (con/sin tilde, acortadas) bajo el término maestro 'Electrónica'
    "electro": "Electrónica", "electronica": "Electrónica", "electrónica": "Electrónica", "electrónic": "Electrónica",
    # Unificación de formatos de separación para el género Hip Hop
    "hip hop": "Hip Hop", "hip-hop": "Hip Hop", "hiphop": "Hip Hop",
    # Corrección de omisión de letras para Jazz y duplicación de consonantes en Metal
    "jazz": "Jazz", "jaz": "Jazz", "metal": "Metal", "metall": "Metal",
    # Corrección de erratas de ordenación de letras en Pop
    "pop": "Pop", "ppo": "Pop", 
    # Unificación del formato comercial del género R&B
    "r&b": "R&B", "r & b": "R&B", "rnb": "R&B",
    # Estandarización de la tilde en el género urbano Reggaetón
    "reggaeton": "Reggaetón", "regueton": "Reggaetón", "reguetón": "Reggaetón",
    # Mapeos directos uno a uno para géneros específicos
    "ska": "Ska", "salsa": "Salsa", 
    # Estandarización de la variante fonética 'tekno' al término correcto 'Techno'
    "techno": "Techno", "tekno": "Techno",
    # Corrección de la 'k' informal en Flamenco
    "flamenco": "Flamenco", "flamenko": "Flamenco", "folk": "Folk",
    # Unificación de variantes gráficas de Indie
    "indie": "Indie", "indy": "Indie", 
    # Corrección de la falta de ortografía ortográfica 'nb' en Cumbia
    "cumbia": "Cumbia", "kunbia": "Cumbia"
}

# Tabla para unificar la nomenclatura de los escenarios del recinto musical
mapeo_escenario = {
    "escenario principal": "Escenario Principal", "principal": "Escenario Principal",
    "escenario 2": "Escenario Secundario", "secundario": "Escenario Secundario",
    "carpa techno": "Carpa Techno"
}

# Categorías normalizadas para los tipos de pases disponibles en la ticketera
mapeo_tipo_entrada = {
    "general": "General", "vip": "VIP", "early bird": "Early Bird", "abono": "Abono Completo"
}

# Homogeneización de los nombres de las pasarelas y métodos financieros de pago
mapeo_metodo_pago = {
    "tarjeta": "Tarjeta", "credit card": "Tarjeta", "paypal": "PayPal", "efectivo": "Efectivo"
}

# Clasificación unificada del nivel de aportación de los patrocinadores económicos
mapeo_categoria = {
    "main sponsor": "Principal", "principal": "Principal", "colaborador": "Colaborador", "partner": "Colaborador"
}

# Diccionario de traducción para indexar nombres de meses (español/inglés) a su entero correspondiente
meses_maestros = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12,
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
}


# ------------------------------------------------------------------------------
# FUNCIONES DE TEXTO Y TRATAMIENTO BASE
# ------------------------------------------------------------------------------

def limpiar_espacios(texto):
    """Elimina espacios en los extremos y colapsa los dobles espacios intermedios."""
    # Control de seguridad: Si el valor recibido es un nulo de Python (None), se retorna un string vacío.
    if texto is None:
        return ""
    # str(texto).split() fragmenta el texto por cualquier espacio en blanco descartando extremos y repetidos; 
    # luego ' '.join() vuelve a unir las palabras separándolas por un único espacio en blanco exacto.
    return " ".join(str(texto).split())


def es_valor_vacio(texto):
    """Determina si una cadena equivale conceptualmente a un dato ausente."""
    # Sanitiza el argumento eliminando espacios y transformando todo el texto a mayúsculas para comparar de forma segura.
    texto_limpio = limpiar_espacios(texto).upper()
    # Lista de cadenas de texto en bruto que representan la ausencia de información en las bases de datos sucias.
    valores_nulos = ["", "N/A", "-", "NO DISPONIBLE", "VACIO", "NONE"]
    # Retorna un booleano (True o False) evaluando si el texto procesado coincide con alguna cadena de la lista.
    return texto_limpio in valores_nulos


def corregir_palabra_tilde(palabra):
    """Busca una palabra individual en el diccionario de tildes o aplica mayúscula inicial."""
    # Convierte la palabra a minúsculas y remueve espacios marginales para estandarizar la consulta en el diccionario.
    palabra_minuscula = palabra.lower().strip()
    # Si la cadena normalizada existe como clave dentro del diccionario de tildes maestras...
    if palabra_minuscula in correcciones_tildes:
        # Se extrae y retorna su versión correctamente acentuada (ej: 'garcia' -> 'García').
        return correcciones_tildes[palabra_minuscula]
    
    # En caso de no requerir tilde forzada, se comprueba si la palabra tiene longitud válida para evitar fallas de índice.
    if len(palabra) > 0:
        # Pone el primer carácter en mayúsculas y concatena el resto de la palabra tal cual venía.
        return palabra[0].upper() + palabra[1:]
    # Si la palabra es un string vacío residual, la devuelve intacta.
    return palabra


def normalizar_texto(texto):
    """Limpia los espacios y aplica las correcciones ortográficas palabra por palabra."""
    # Si el campo supera el test de valor vacío, se asume la ausencia del dato y se estandariza como 'SIN DATOS'.
    if es_valor_vacio(texto):
        return "SIN DATOS"
    
    # Limpia los espacios corruptos y fragmenta la cadena completa en una lista de palabras individuales utilizando split().
    palabras = limpiar_espacios(texto).split()
    # List comprehension que itera palabra por palabra, aplicando la función de corrección y capitalización ortográfica.
    palabras_corregidas = [corregir_palabra_tilde(palabra_individual) for palabra_individual in palabras]
    # Reconstruye y retorna el string de texto unificado intercalando un único espacio entre cada elemento de la lista.
    return " ".join(palabras_corregidas)


# ------------------------------------------------------------------------------
# FUNCIONES DE PAÍSES Y CATEGORÍAS
# ------------------------------------------------------------------------------

def normalizar_pais(valor_pais):
    """Transforma y unifica el nombre de un país utilizando el diccionario de mapeo maestro."""
    # Control preventivo: Si la celda contiene un nulo nativo, se devuelve la bandera estándar de ausencia.
    if valor_pais is None:
        return "SIN DATOS"
    
    # Convierte la variable en string de texto, elimina espacios terminales y fuerza la cadena a minúsculas.
    pais_limpio = str(valor_pais).strip().lower()
    
    # Evaluación manual de palabras nulas en bruto antes de proceder con las claves del diccionario.
    if pais_limpio in ["", "n/a", "-", "no disponible", "vacio", "none"]:
        return "SIN DATOS"
        
    # Si el término normalizado existe dentro de las claves registradas en el diccionario de países...
    if pais_limpio in mapeo_paises:
        # Retorna el nombre geográfico oficial (ej: 'usa' o 'ee.uu.' devuelven rigurosamente 'Estados Unidos').
        return mapeo_paises[pais_limpio]
        
    # Registra una traza de aviso en la terminal para advertir al analista que un país nuevo no está contemplado en el diccionario.
    print(f"AVISO: País no reconocido en el mapeo maestro → '{valor_pais}'")
    # Devuelve el valor original quitando espacios y capitalizando la primera letra de cada palabra como plan de contingencia.
    return valor_pais.strip().title()


def normalizar_categoria(valor, diccionario_mapeo, campo_nombre="categoria"):
    """Normaliza un campo categórico cruzándolo con su diccionario de mapeo."""
    # Comprobación de seguridad en cascada para detectar nulos físicos, valores vacíos lógicos o textos marcados previamente.
    if valor is None or es_valor_vacio(str(valor)) or valor == "SIN DATOS":
        return "SIN DATOS"
        
    # Remueve espacios periféricos y pasa la cadena a minúsculas para igualar el formato de búsqueda del diccionario.
    valor_limpio = str(valor).lower().strip()
    
    # Si la categoría sucia del archivo se encuentra registrada en el mapeo específico pasado por argumento...
    if valor_limpio in diccionario_mapeo:
        # Devuelve el valor estandarizado unificado del festival.
        return diccionario_mapeo[valor_limpio]
    
    # Si el valor ingresado es desconocido, se imprime una alerta indicando la columna afectada.
    print(f"AVISO: Valor no reconocido en {campo_nombre} → '{valor}'")
    # Retorna la cadena original sin alterar para no destruir información que requira posterior inspección manual.
    return valor


# ------------------------------------------------------------------------------
# FUNCIONES DE NÚMEROS Y MONEDAS
# ------------------------------------------------------------------------------

def limpiar_simbolos_moneda(cadena):
    """Quita los caracteres de divisa y espacios en blanco internos."""
    # Encadena reemplazos de texto de manera secuencial para purgar símbolos de euros, dólares y espacios en blanco tradicionales.
    return cadena.replace('€', '').replace('$', '').replace(' ', '')


def unificar_separadores_decimales(cadena):
    """Transforma formatos numéricos europeos (puntos en miles, comas en decimales) a estándar."""
    # Si conviven simultáneamente comas y puntos (ej: '2.500,50' -> Formato Europeo / Latino).
    if ',' in cadena and '.' in cadena:
        cadena = cadena.replace('.', '')  # Se elimina el punto que actúa como separador estético de miles.
        cadena = cadena.replace(',', '.')  # Se sustituye la coma decimal por el punto, que es el operador matemático de Python.
    # Si solo existe una coma en la cadena sin presencia de puntos (ej: '1500,75').
    elif ',' in cadena:
        cadena = cadena.replace(',', '.') # Transforma la coma en punto decimal estándar.
    # Retorna el string numérico depurado listo para ser interpretado de manera nativa por la máquina.
    return cadena


def limpiar_valor_numerico(valor):
    """Transforma de manera segura importes sucios a float."""
    # Valida si la celda está vacía o es None; en tal caso, devuelve un nulo matemático para no adulterar cálculos estadísticos.
    if valor is None or es_valor_vacio(str(valor)):
        return None
    
    # Inicializa el procesamiento forzando la conversión a string y suprimiendo espacios laterales.
    procesado = str(valor).strip()
    # Llama a la subfunción para eliminar caracteres monetarios residuales (€, $, etc.).
    procesado = limpiar_simbolos_moneda(procesado)
    # Llama a la subfunción para resolver las discrepancias de formato regional de comas y puntos.
    procesado = unificar_separadores_decimales(procesado)
    
    # Bloque de captura de excepciones para salvaguardar la ejecución frente a cadenas no numéricas corruptas.
    try:
        # Intenta castear el string limpio a un tipo primitivo float de precisión real.
        return float(procesado)
    except ValueError:
        # Si la cadena contenía letras u otros símbolos incorregibles, captura el error de valor y devuelve None de forma segura.
        return None


# ------------------------------------------------------------------------------
# FUNCIONES DE IDENTIFICADORES Y DNI
# ------------------------------------------------------------------------------

def limpiar_id(identificador):
    """Estandariza códigos de identificación a minúsculas sin espacios."""
    # Comprobación de nulos; si es verdadero, se le asigna el rótulo unificado de advertencia.
    if identificador is None or es_valor_vacio(str(identificador)):
        return "SIN DATOS"
    # Elimina los espacios de los bordes y pasa toda la cadena de código a minúsculas (ej: 'ART-021' -> 'art-021').
    return str(identificador).strip().lower()


def limpiar_dni(documento_nacional_identidad):
    """Aplica el rellenado con ceros a la izquierda y valida la estructura."""
    # Validación de existencia; si el DNI es nulo, retorna la etiqueta común.
    if documento_nacional_identidad is None or es_valor_vacio(str(documento_nacional_identidad)):
        return "SIN DATOS"
    
    # Sanitiza eliminando espacios laterales y obligando a la letra del documento a estar en mayúsculas.
    dni_limpio = str(documento_nacional_identidad).strip().upper()
    # zfill(9) rellena el string insertando ceros a la izquierda hasta que la longitud total sea exactamente de 9 caracteres.
    dni_formateado = dni_limpio.zfill(9)
    
    # Slicing: Extrae los primeros 8 caracteres de la cadena, correspondientes teóricamente a la numeración del DNI.
    parte_numerica = dni_formateado[:8]
    # Slicing: Extrae el último carácter de la cadena, correspondiente a la letra de control del DNI.
    parte_letra = dni_formateado[-1]
    
    # Comprobación estricta de integridad formal: longitud 9, bloque inicial numérico y terminación alfabética.
    if len(dni_formateado) == 9 and parte_numerica.isdigit() and parte_letra.isalpha():
        # Si la estructura es correcta, se retorna el DNI perfectamente normalizado.
        return dni_formateado
    
    # Si no supera las tres reglas básicas de validación, imprime una alarma crítica en la consola del sistema.
    print(f"AVISO CRÍTICO: Estructura de DNI corrupta detectada → '{documento_nacional_identidad}'")
    # Retorna la bandera que avisa al analista que debe intervenir esa fila de forma humana durante la auditoría.
    return "REVISAR MANUALMENTE"


# ------------------------------------------------------------------------------
# FUNCIONES DE TRATAMIENTO DE FECHAS 
# ------------------------------------------------------------------------------

def formato_texto_largo(cadena):
    """Procesa formato: 'DD de mes de AAAA' (ej. 15 de julio de 2026)."""
    # Segmenta la cadena tomando el literal invariable ' de ' como patrón de división.
    partes = cadena.split(" de ")
    # Si la división produce exactamente 3 fragmentos (día, mes, año)...
    if len(partes) == 3:
        try:
            # Convierte el bloque de texto del día en un entero numérico.
            dia = int(partes[0].strip())
            # Busca en el diccionario de meses el índice correspondiente a la cadena del mes en minúsculas.
            mes = meses_maestros.get(partes[1].strip().lower())
            # Convierte el bloque de texto del año en un entero numérico.
            anio = int(partes[2].strip())
            # Devuelve los tres elementos desempaquetados.
            return dia, mes, anio
        except ValueError:
            # Captura fallos si el día o año contenían letras incorregibles, ignorándolos para avanzar.
            pass
    # Si el formato falla, devuelve una tupla de tres nulos estructurales.
    return None, None, None


def formato_americano(cadena):
    """Procesa formato: 'mes DD, AAAA' (ej. julio 15, 2026)."""
    # Suprime la coma característica del formato de fecha estadounidense para no distorsionar el casteo numérico del día.
    cadena_limpia = cadena.replace(",", "")
    # Divide por defecto la cadena utilizando los espacios en blanco restantes como separadores.
    partes = tuple(cadena_limpia.split())
    # Valida que se hayan obtenido los tres elementos temporales básicos.
    if len(partes) == 3:
        try:
            # El primer elemento corresponde al literal del mes; se consulta su entero numérico en la tabla de traducción.
            mes = meses_maestros.get(partes[0].strip().lower())
            # Convierte el segundo bloque de texto (día) a entero.
            dia = int(partes[1].strip())
            # Convierte el tercer bloque de texto (año) a entero.
            anio = int(partes[2].strip())
            # Retorna el trío de valores resuelto.
            return dia, mes, anio
        except ValueError:
            # Captura y salta errores si los datos numéricos vienen corruptos de origen.
            pass
    # Retorna nulos si la estructura de la cadena no encajaba con el formato americano esperado.
    return None, None, None


def formato_guiones(cadena):
    """Procesa formatos basados en guiones: AAAA-MM-DD o DD-MM-AAAA."""
    # Divide el texto utilizando el guion medio como carácter delimitador.
    partes = cadena.split("-")
    # Confirma que la cadena se subdivida en tres secciones lógicas.
    if len(partes) == 3:
        try:
            # Comprobación de orden: Si el primer elemento mide 4 dígitos, es un formato internacional ISO (AAAA-MM-DD).
            if len(partes[0].strip()) == 4:
                anio = int(partes[0].strip())
                mes = int(partes[1].strip())
                dia = int(partes[2].strip())
            # Si mide diferente, se asume un ordenamiento convencional/humano (DD-MM-AAAA o DD-mes-AAAA).
            else:
                dia = int(partes[0].strip())
                # Captura el elemento central reduciendo espacios y forzando minúsculas.
                centro = partes[1].strip().lower()
                # Expresión ternaria: Si el mes es numérico lo castea a entero; si viene en texto ('aug', 'feb'), lo traduce usando meses_maestros.
                mes = int(centro) if centro.isdigit() else meses_maestros.get(centro)
                anio = int(partes[2].strip())
            # Devuelve los elementos debidamente ordenados.
            return dia, mes, anio
        except ValueError:
            pass
    return None, None, None


def formato_barras(cadena):
    """Procesa formatos basados en barras: DD/MM/AAAA o DD/M/AA."""
    # Divide la cadena de texto usando el operador de barra inclinada como delimitador oficial.
    partes = cadena.split("/")
    # Comprueba la existencia de los tres componentes cronológicos obligatorios.
    if len(partes) == 3:
        try:
            # Castea a entero el fragmento inicial asignándolo a la variable del día.
            dia = int(partes[0].strip())
            # Castea a entero el fragmento medio asignándolo a la variable del mes.
            mes = int(partes[1].strip())
            # Almacena de manera provisional la cadena del año para validar su longitud.
            anio_cadena = partes[2].strip()
            # Si el año viene abreviado a dos posiciones (ej: '26'), le suma el siglo (2000) para expandirlo a '2026'; si no, lo convierte directo.
            anio = int(anio_cadena) + 2000 if len(anio_cadena) == 2 else int(anio_cadena)
            # Retorna las variables numéricas finales listas.
            return dia, mes, anio
        except ValueError:
            pass
    return None, None, None


def normalizar_fecha(fecha_texto):
    """Función unificadora que enruta la cadena hacia su analizador correspondiente."""
    # Si la celda carece de valor o es vacía, interrumpe el flujo devolviendo directamente la bandera de anomalía cronológica.
    if fecha_texto is None or es_valor_vacio(str(fecha_texto)):
        return "FECHA INVÁLIDA"
        
    # Inicializa la unificación limpiando espacios terminales y forzando las letras a minúsculas.
    cadena = str(fecha_texto).strip().lower()
    # Inicializa las tres variables receptoras en nulo.
    dia, mes, anio = None, None, None

    # Enrutador heurístico basado en sub-cadenas y patrones de caracteres delimitadores
    if " de " in cadena:
        dia, mes, anio = formato_texto_largo(cadena)
    elif "," in cadena:
        dia, mes, anio = formato_americano(cadena)
    elif "-" in cadena:
        dia, mes, anio = formato_guiones(cadena)
    elif "/" in cadena:
        dia, mes, anio = formato_barras(cadena)

    # Evaluación post-enrutamiento: Valida que ninguna variable haya quedado en nulo tras pasar por las funciones.
    if dia is not None and mes is not None and anio is not None:
        # Validación de reglas lógicas del calendario (rangos válidos de días, meses y años históricos positivos).
        if 1 <= dia <= 31 and 1 <= mes <= 12 and anio > 0:
            # Formatea y retorna la fecha en un string unificado estricto con relleno de ceros (DD/MM/AAAA).
            return f"{dia:02d}/{mes:02d}/{anio}"
            
    # Si las variables contienen nulos o violan los rangos del calendario, emite una traza de advertencia por consola.
    print(f"AVISO: Estructura de fecha no reconocida → '{fecha_texto}'")
    # Retorna la etiqueta estándar de error cronológico para informar en el reporte final.
    return "FECHA INVÁLIDA"


# ------------------------------------------------------------------------------
# FILTRADO E INTEGRIDAD LOGICA
# ------------------------------------------------------------------------------

def contar_vacios(registro):
    """Cuenta cuántos campos vacíos o marcados con alertas tiene un diccionario."""
    # Lista de cadenas que representan celdas que no aportaron información válida o que contienen fallos insalvables.
    alertas_vacio = ["", "SIN DATOS", "FECHA INVÁLIDA", "REVISAR MANUALMENTE", None]
    # Itera por los valores internos del diccionario, sumando 1 por cada coincidencia exacta con la lista de alertas.
    return sum(1 for valor in registro.values() if valor in alertas_vacio)


def eliminar_duplicados(datos, campos_clave):
    """Elimina duplicados manteniendo el registro que contenga mayor cantidad de información."""
    # Diccionario hash intermedio que guardará la fila óptima indexada por su clave compuesta unificada.
    tabla_unicos = {}
    # Contador acumulativo para rastrear cuántas filas repetidas/redundantes han sido dadas de baja en el proceso.
    conteo_eliminados = 0
    
    # Itera secuencialmente sobre cada diccionario (registro/fila) del conjunto de datos cargado.
    for registro in datos:
        # Genera una tupla inmutable (clave compuesta) extrayendo, limpiando y pasando a minúsculas los campos clave definidos.
        clave = tuple(str(registro.get(campo, "")).lower().strip() for campo in campos_clave)
        # Calcula el indicador de calidad actual (cantidad de celdas vacías o erróneas en esta fila específica).
        vacios_actual = contar_vacios(registro)
        
        # Si la tupla clave ya existe como índice dentro de nuestra estructura hash...
        if clave in tabla_unicos:
            # Se incrementa inmediatamente el contador general de elementos duplicados detectados.
            conteo_eliminados += 1
            # Se evalúa la calidad de la fila que guardamos previamente en esa misma posición del diccionario.
            vacios_guardado = contar_vacios(tabla_unicos[clave])
            # Algoritmo de desempate inteligente: Si la fila nueva tiene MENOS campos vacíos que la almacenada...
            if vacios_actual < vacios_guardado:
                # Se sobreescribe la clave de la tabla, conservando la fila más rica en información y desechando la incompleta.
                tabla_unicos[clave] = registro
        else:
            # Si es la primera vez que se procesa esta clave compuesta, se almacena el registro de manera directa.
            tabla_unicos[clave] = registro
            
    # Retorna una tupla conteniendo: 1) La lista limpia consolidada sin duplicados y 2) El entero con el total de bajas.
    return list(tabla_unicos.values()), conteo_eliminados