import re

# ── TEXTO ─────────────────────────────────────────────────────────────────────

CORRECCIONES_TILDES = {
    'jose': 'José', 'garcia': 'García', 'maria': 'María',
    'gonzalez': 'González', 'martinez': 'Martínez', 'lopez': 'López',
    'perez': 'Pérez', 'sanchez': 'Sánchez', 'gomez': 'Gómez',
    'fernandez': 'Fernández', 'rodriguez': 'Rodríguez', 'hernandez': 'Hernández',
    'jimenez': 'Jiménez', 'diaz': 'Díaz',
}


def limpiar_texto(texto):
    if texto is None:
        return ''
    return re.sub(r' +', ' ', str(texto).strip())


def normalizar_texto(texto):
    limpio = limpiar_texto(texto)
    if not limpio:
        return limpio
    resultado = limpio.title()
    for sin_tilde, con_tilde in CORRECCIONES_TILDES.items():
        resultado = re.sub(r'\b' + sin_tilde + r'\b', con_tilde, resultado, flags=re.IGNORECASE)
    return resultado


def aplicar_limpiar_texto(datos, campos, nombre_fichero):
    contador = {c: 0 for c in campos}
    for registro in datos:
        for campo in campos:
            v = registro.get(campo)
            if v is not None:
                limpio = limpiar_texto(str(v))
                if limpio != str(v):
                    registro[campo] = limpio
                    contador[campo] += 1
    for campo, n in contador.items():
        if n:
            print(f"  {nombre_fichero} > {campo}: {n} textos corregidos")
    return datos


# ── VALORES VACÍOS ────────────────────────────────────────────────────────────

def es_vacio(valor):
    if valor is None:
        return True
    return str(valor).strip().lower() in {'', 'n/a', '-', 'no disponible', 'none', 'sin datos'}


# ── NUMÉRICO ──────────────────────────────────────────────────────────────────

def limpiar_valor_numerico(valor):
    if valor is None:
        return None
    texto = str(valor).strip()
    texto = re.sub(r'[€$£\s]', '', texto)
    texto = re.sub(r'\s*(min|eur|usd)\s*$', '', texto, flags=re.IGNORECASE)
    # "15.000,50" → punto miles, coma decimal → "15000.50"
    if re.match(r'^\d{1,3}(\.\d{3})+(,\d+)?$', texto):
        texto = texto.replace('.', '').replace(',', '.')
    # "272,939" → coma miles → "272939"
    elif re.match(r'^\d{1,3}(,\d{3})+(\.\d+)?$', texto):
        texto = texto.replace(',', '')
    else:
        texto = texto.replace(',', '.')
    m = re.match(r'^-?\d+\.?\d*', texto)
    if m:
        texto = m.group(0)
    try:
        numero = float(texto)
        return int(numero) if numero == int(numero) else numero
    except (ValueError, OverflowError):
        return None


# ── FECHAS Y HORAS ────────────────────────────────────────────────────────────

MESES_ES = {
    'enero': '01', 'ene': '01', 'january': '01', 'jan': '01',
    'febrero': '02', 'feb': '02', 'february': '02',
    'marzo': '03', 'mar': '03', 'march': '03',
    'abril': '04', 'abr': '04', 'april': '04',
    'mayo': '05', 'may': '05',
    'junio': '06', 'jun': '06', 'june': '06',
    'julio': '07', 'jul': '07', 'july': '07',
    'agosto': '08', 'ago': '08', 'august': '08',
    'septiembre': '09', 'sep': '09', 'sept': '09', 'september': '09',
    'octubre': '10', 'oct': '10', 'october': '10',
    'noviembre': '11', 'nov': '11', 'november': '11',
    'diciembre': '12', 'dic': '12', 'december': '12',
}


def _anio_completo(s):
    a = int(s)
    return a + 2000 if a < 100 else a


def normalizar_fecha(texto):
    if not texto or str(texto).strip() in ('', 'None', 'N/A', '-'):
        return 'FECHA INVÁLIDA'
    t = str(texto).strip()

    # YYYY-MM-DD
    m = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})$', t)
    if m:
        return f"{int(m.group(3)):02d}/{int(m.group(2)):02d}/{m.group(1)}"

    # DD/MM/YYYY o DD/MM/YY
    m = re.match(r'^(\d{1,2})/(\d{1,2})/(\d{2,4})$', t)
    if m:
        return f"{int(m.group(1)):02d}/{int(m.group(2)):02d}/{_anio_completo(m.group(3))}"

    # DD-MM-YYYY o DD-MM-YY
    m = re.match(r'^(\d{1,2})-(\d{1,2})-(\d{2,4})$', t)
    if m:
        return f"{int(m.group(1)):02d}/{int(m.group(2)):02d}/{_anio_completo(m.group(3))}"

    # DD-mon-YYYY  (15-jul-2026, 16-feb-2025)
    m = re.match(r'^(\d{1,2})-([a-záéíóú]+)-(\d{2,4})$', t, re.IGNORECASE)
    if m:
        mes = MESES_ES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(1)):02d}/{mes}/{_anio_completo(m.group(3))}"

    # "15 de julio de 2026"
    m = re.match(r'^(\d{1,2})\s+de\s+([a-záéíóú]+)\s+de\s+(\d{2,4})$', t, re.IGNORECASE)
    if m:
        mes = MESES_ES.get(m.group(2).lower())
        if mes:
            return f"{int(m.group(1)):02d}/{mes}/{_anio_completo(m.group(3))}"

    # "julio 15, 2026" o "septiembre 31, 2026"
    m = re.match(r'^([a-záéíóú]+)\s+(\d{1,2}),\s*(\d{2,4})$', t, re.IGNORECASE)
    if m:
        mes = MESES_ES.get(m.group(1).lower())
        if mes:
            return f"{int(m.group(2)):02d}/{mes}/{_anio_completo(m.group(3))}"

    print(f"  AVISO: no se pudo convertir la fecha '{t}'")
    return 'FECHA INVÁLIDA'


def normalizar_hora(texto):
    if not texto or str(texto).strip() in ('', 'None', 'N/A'):
        return ''
    t = str(texto).strip()

    # "2100" o "1800" → "21:00"
    if re.match(r'^\d{3,4}$', t):
        t = t.zfill(4)
        return f"{t[:2]}:{t[2:]}"

    # "16.00" → "16:00"
    m = re.match(r'^(\d{1,2})\.(\d{2})$', t)
    if m:
        return f"{int(m.group(1)):02d}:{m.group(2)}"

    # "8:00 PM" → "20:00"
    m = re.match(r'^(\d{1,2}):(\d{2})\s*(AM|PM)$', t, re.IGNORECASE)
    if m:
        h, mn, ampm = int(m.group(1)), m.group(2), m.group(3).upper()
        if ampm == 'PM' and h != 12:
            h += 12
        elif ampm == 'AM' and h == 12:
            h = 0
        return f"{h:02d}:{mn}"

    # "15:30" ya correcto
    if re.match(r'^\d{1,2}:\d{2}$', t):
        partes = t.split(':')
        return f"{int(partes[0]):02d}:{partes[1]}"

    return t


# ── CATEGORÍAS ────────────────────────────────────────────────────────────────

_SENTINEL = {'sin datos', 'revisar manualmente', 'sin referencia', 'fecha inválida'}


def normalizar_categoria(valor, mapeo):
    if valor is None:
        return valor
    limpio = limpiar_texto(str(valor))
    if limpio.lower() in _SENTINEL:
        return limpio
    clave = limpio.lower()
    if clave in mapeo:
        return mapeo[clave]
    print(f"  AVISO: valor no reconocido en categoría: '{valor}'")
    return limpio
