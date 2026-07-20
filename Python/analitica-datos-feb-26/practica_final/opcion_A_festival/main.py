import os
from datetime import date

from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml
from lib.limpieza import (
    aplicar_limpiar_texto, es_vacio, limpiar_texto,
    limpiar_valor_numerico, normalizar_categoria, normalizar_fecha, normalizar_hora,
)
from lib.auditoria import auditar_fichero, detectar_fuera_de_rango, eliminar_duplicados
from lib.exportacion import exportar_csv, exportar_excel, guardar_informe

DIR = os.path.dirname(__file__)
DATOS = os.path.join(DIR, 'datos')
LIMPIOS = os.path.join(DIR, 'datos_limpios')

# ── MAPPINGS ──────────────────────────────────────────────────────────────────

MAPEO_GENEROS = {
    'rock': 'Rock', 'rokc': 'Rock', 'roc': 'Rock',
    'pop': 'Pop', 'ppo': 'Pop',
    'jazz': 'Jazz', 'jaz': 'Jazz',
    'hip hop': 'Hip-Hop', 'hip-hop': 'Hip-Hop', 'hiphop': 'Hip-Hop',
    'electrónica': 'Electrónica', 'electronica': 'Electrónica',
    'electrónic': 'Electrónica', 'electro': 'Electrónica',
    'metal': 'Metal', 'metall': 'Metal',
    'techno': 'Techno', 'tekno': 'Techno',
    'reggaetón': 'Reggaetón', 'reggaeton': 'Reggaetón',
    'regueton': 'Reggaetón', 'reguetón': 'Reggaetón',
    'flamenco': 'Flamenco', 'flamenko': 'Flamenco',
    'indie': 'Indie', 'indy': 'Indie',
    'folk': 'Folk',
    'salsa': 'Salsa',
    'ska': 'Ska',
    'cumbia': 'Cumbia', 'kunbia': 'Cumbia',
    'r&b': 'R&B', 'r & b': 'R&B', 'rnb': 'R&B',
}

MAPEO_PAISES = {
    'españa': 'España', 'espana': 'España', 'espña': 'España',
    'argentina': 'Argentina', 'argetina': 'Argentina',
    'brasil': 'Brasil', 'brazil': 'Brasil',
    'chile': 'Chile',
    'colombia': 'Colombia', 'kolombia': 'Colombia',
    'cuba': 'Cuba',
    'ee.uu.': 'EE.UU.', 'estados unidos': 'EE.UU.', 'usa': 'EE.UU.', 'us': 'EE.UU.',
    'francia': 'Francia', 'france': 'Francia',
    'italia': 'Italia',
    'méxico': 'México', 'mexico': 'México', 'mejico': 'México',
    'perú': 'Perú', 'peru': 'Perú',
    'portugal': 'Portugal',
    'reino unido': 'Reino Unido', 'uk': 'Reino Unido',
    'r. unido': 'Reino Unido', 'united kingdom': 'Reino Unido',
    'venezuela': 'Venezuela',
    'rep. dominicana': 'Rep. Dominicana', 'r. dominicana': 'Rep. Dominicana',
    'rd': 'Rep. Dominicana', 'republica dominicana': 'Rep. Dominicana',
}

MAPEO_ESCENARIOS = {
    'escenario principal': 'Escenario Principal',
    'esc. principal': 'Escenario Principal',
    'main stage': 'Escenario Principal',
    'escenario río': 'Escenario Río', 'escenario rio': 'Escenario Río',
    'esc. río': 'Escenario Río', 'esc. rio': 'Escenario Río',
    'escenario sol': 'Escenario Sol', 'esc. sol': 'Escenario Sol',
    'escenario luna': 'Escenario Luna', 'esc. luna': 'Escenario Luna',
    'escenario bosque': 'Escenario Bosque', 'esc. bosque': 'Escenario Bosque',
}

MAPEO_TIPO_ENTRADA = {
    'general': 'General', 'gral': 'General', 'gral.': 'General',
    'premium': 'Premium', 'premiun': 'Premium', 'prémium': 'Premium',
    'vip': 'VIP', 'v.i.p.': 'VIP',
    'abono': 'Abono',
}

MAPEO_METODO_PAGO = {
    'paypal': 'PayPal', 'pay pal': 'PayPal',
    'tarjeta': 'Tarjeta', 'tarjeta de crédito': 'Tarjeta',
    'tarjeta credito': 'Tarjeta', 'visa': 'Tarjeta',
    'transferencia': 'Transferencia', 'transferencia bancaria': 'Transferencia',
    'transfer.': 'Transferencia',
    'efectivo': 'Efectivo', 'cash': 'Efectivo',
    'metálico': 'Efectivo', 'metalico': 'Efectivo',
    'bizum': 'Bizum', 'bisum': 'Bizum',
}

MAPEO_CATEGORIA_PATROCINADOR = {
    'platinum': 'Platinum', 'platino': 'Platinum',
    'gold': 'Gold', 'oro': 'Gold',
    'silver': 'Silver', 'plata': 'Silver',
    'bronze': 'Bronce', 'bronce': 'Bronce',
}

# ── FASE 1 ────────────────────────────────────────────────────────────────────

def fase1_carga():
    print("\n" + "=" * 60)
    print("FASE 1: CARGA DE DATOS")
    print("=" * 60)

    artistas = cargar_csv(os.path.join(DATOS, 'artistas.csv'))
    horarios = cargar_excel(os.path.join(DATOS, 'escenarios_horarios.xlsx'))
    ventas = cargar_json(os.path.join(DATOS, 'ventas_entradas.json'))
    patrocinadores = cargar_xml(os.path.join(DATOS, 'patrocinadores.xml'), 'patrocinador')

    for nombre, datos in [
        ('artistas.csv', artistas),
        ('escenarios_horarios.xlsx', horarios),
        ('ventas_entradas.json', ventas),
        ('patrocinadores.xml', patrocinadores),
    ]:
        print(f"\n--- {nombre} ---")
        print(f"  Registros: {len(datos)}")
        print(f"  Campos: {list(datos[0].keys()) if datos else []}")
        print("  Primeros 5 registros:")
        for r in datos[:5]:
            print(f"    {r}")

    return artistas, horarios, ventas, patrocinadores

# ── FASE 2 ────────────────────────────────────────────────────────────────────

def fase2_auditoria(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 2: AUDITORÍA DE CALIDAD")
    print("=" * 60)

    return (
        auditar_fichero(artistas, 'artistas.csv'),
        auditar_fichero(horarios, 'escenarios_horarios.xlsx'),
        auditar_fichero(ventas, 'ventas_entradas.json'),
        auditar_fichero(patrocinadores, 'patrocinadores.xml'),
    )

# ── FASE 3 ────────────────────────────────────────────────────────────────────

def fase3_texto(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 3: LIMPIEZA DE TEXTO Y ESPACIOS")
    print("=" * 60)

    aplicar_limpiar_texto(artistas,
        ['nombre', 'genero_musical', 'pais', 'email_manager', 'telefono'],
        'artistas.csv')
    aplicar_limpiar_texto(horarios,
        ['escenario', 'artista', 'hora_inicio', 'hora_fin', 'soundcheck', 'notas'],
        'escenarios_horarios.xlsx')
    aplicar_limpiar_texto(ventas,
        ['nombre_comprador', 'email', 'tipo_entrada', 'metodo_pago'],
        'ventas_entradas.json')
    aplicar_limpiar_texto(patrocinadores,
        ['nombre_empresa', 'contacto', 'email', 'categoria'],
        'patrocinadores.xml')

    return artistas, horarios, ventas, patrocinadores

# ── FASE 4 ────────────────────────────────────────────────────────────────────

def fase4_tipos_y_vacios(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 4: TIPOS Y VALORES VACÍOS")
    print("=" * 60)

    n = sum(1 for r in artistas if r.get('cache_eur') is not None)
    for r in artistas:
        r['cache_eur'] = limpiar_valor_numerico(r.get('cache_eur'))
        if es_vacio(r.get('email_manager')):
            r['email_manager'] = 'SIN DATOS'
        if es_vacio(r.get('telefono')):
            r['telefono'] = 'SIN DATOS'
    print(f"  artistas.csv > cache_eur: {n} valores convertidos a número")
    print(f"  artistas.csv > email_manager/telefono: vacíos → 'SIN DATOS'")

    n = sum(1 for r in ventas if r.get('precio') is not None)
    for r in ventas:
        r['precio'] = limpiar_valor_numerico(r.get('precio'))
        if es_vacio(r.get('dni')):
            r['dni'] = 'SIN DATOS'
        if es_vacio(r.get('metodo_pago')):
            r['metodo_pago'] = 'SIN DATOS'
    print(f"  ventas_entradas.json > precio: {n} valores convertidos a número")

    n = sum(1 for r in patrocinadores if r.get('importe_patrocinio') is not None)
    for r in patrocinadores:
        r['importe_patrocinio'] = limpiar_valor_numerico(r.get('importe_patrocinio'))
    print(f"  patrocinadores.xml > importe_patrocinio: {n} valores convertidos a número")

    return artistas, horarios, ventas, patrocinadores

# ── FASE 5 ────────────────────────────────────────────────────────────────────

def fase5_categorias(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 5: NORMALIZACIÓN DE CATEGORÍAS")
    print("=" * 60)

    def normalizar_campo(datos, campo, mapeo, nombre):
        antes = sorted(set(limpiar_texto(str(r.get(campo) or '')) for r in datos))
        for r in datos:
            r[campo] = normalizar_categoria(r.get(campo), mapeo)
        despues = sorted(set(str(r.get(campo) or '') for r in datos))
        print(f"  {nombre} > {campo}")
        print(f"    ANTES  ({len(antes)} valores): {antes[:6]}{'...' if len(antes) > 6 else ''}")
        print(f"    DESPUÉS ({len(despues)} valores): {despues}")

    normalizar_campo(artistas, 'genero_musical', MAPEO_GENEROS, 'artistas.csv')
    normalizar_campo(artistas, 'pais', MAPEO_PAISES, 'artistas.csv')
    normalizar_campo(horarios, 'escenario', MAPEO_ESCENARIOS, 'escenarios_horarios.xlsx')
    normalizar_campo(ventas, 'tipo_entrada', MAPEO_TIPO_ENTRADA, 'ventas_entradas.json')
    normalizar_campo(ventas, 'metodo_pago', MAPEO_METODO_PAGO, 'ventas_entradas.json')
    normalizar_campo(patrocinadores, 'categoria', MAPEO_CATEGORIA_PATROCINADOR, 'patrocinadores.xml')

    return artistas, horarios, ventas, patrocinadores

# ── FASE 6 ────────────────────────────────────────────────────────────────────

def fase6_fechas_y_horas(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 6: NORMALIZACIÓN DE FECHAS Y HORAS")
    print("=" * 60)

    def normalizar_campo_fecha(datos, campo, nombre):
        ok = err = 0
        for r in datos:
            v = r.get(campo)
            if v and not es_vacio(v):
                nueva = normalizar_fecha(str(v))
                r[campo] = nueva
                if nueva == 'FECHA INVÁLIDA':
                    err += 1
                else:
                    ok += 1
        print(f"  {nombre} > {campo}: {ok} normalizadas, {err} inválidas")

    def normalizar_campo_hora(datos, campo, nombre):
        n = 0
        for r in datos:
            v = r.get(campo)
            if v and not es_vacio(v):
                nueva = normalizar_hora(str(v))
                if nueva != str(v):
                    r[campo] = nueva
                    n += 1
        print(f"  {nombre} > {campo}: {n} horas normalizadas")

    normalizar_campo_fecha(horarios, 'fecha', 'escenarios_horarios.xlsx')
    normalizar_campo_hora(horarios, 'hora_inicio', 'escenarios_horarios.xlsx')
    normalizar_campo_hora(horarios, 'hora_fin', 'escenarios_horarios.xlsx')
    normalizar_campo_hora(horarios, 'soundcheck', 'escenarios_horarios.xlsx')
    normalizar_campo_fecha(ventas, 'fecha_compra', 'ventas_entradas.json')
    normalizar_campo_fecha(patrocinadores, 'fecha_inicio', 'patrocinadores.xml')
    normalizar_campo_fecha(patrocinadores, 'fecha_fin', 'patrocinadores.xml')

    return artistas, horarios, ventas, patrocinadores

# ── FASE 7 ────────────────────────────────────────────────────────────────────

def fase7_duplicados(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 7: ELIMINACIÓN DE DUPLICADOS")
    print("=" * 60)

    def dedup(datos, campos, nombre):
        antes = len(datos)
        datos = eliminar_duplicados(datos, campos)
        print(f"  {nombre}: {antes - len(datos)} duplicados eliminados ({antes} → {len(datos)} registros)")
        return datos

    artistas = dedup(artistas, ['nombre'], 'artistas.csv')
    horarios = dedup(horarios, ['escenario', 'fecha', 'hora_inicio'], 'escenarios_horarios.xlsx')
    ventas = dedup(ventas, ['id_venta'], 'ventas_entradas.json')
    patrocinadores = dedup(patrocinadores, ['nombre_empresa'], 'patrocinadores.xml')

    return artistas, horarios, ventas, patrocinadores

# ── FASE 8 ────────────────────────────────────────────────────────────────────

def fase8_rangos(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 8: VALORES FUERA DE RANGO")
    print("=" * 60)

    def corregir_rango(datos, campo, minimo, maximo, nombre):
        for i, r in enumerate(datos):
            v = r.get(campo)
            if v is None or not isinstance(v, (int, float)):
                continue
            if detectar_fuera_de_rango(v, minimo, maximo):
                if v < 0:
                    r[campo] = abs(v)
                    print(f"  CORREGIDO {nombre} reg.{i}: {campo} {v} → {abs(v)}")
                else:
                    r[campo] = 'REVISAR MANUALMENTE'
                    print(f"  FUERA DE RANGO {nombre} reg.{i}: {campo} = {v}")

    corregir_rango(artistas, 'cache_eur', 500, 500_000, 'artistas.csv')
    corregir_rango(ventas, 'precio', 20, 500, 'ventas_entradas.json')
    corregir_rango(patrocinadores, 'importe_patrocinio', 1_000, 1_000_000, 'patrocinadores.xml')

    return artistas, horarios, ventas, patrocinadores

# ── FASE 9 ────────────────────────────────────────────────────────────────────

def fase9_validacion_cruzada(artistas, horarios, ventas, patrocinadores):
    print("\n" + "=" * 60)
    print("FASE 9: VALIDACIÓN CRUZADA")
    print("=" * 60)

    inconsistencias = []
    nombres_artistas = {limpiar_texto(r['nombre']).lower(): r['nombre'] for r in artistas}

    for r in horarios:
        artista_limpio = limpiar_texto(str(r.get('artista') or '')).lower()
        if not artista_limpio:
            continue
        if artista_limpio in nombres_artistas:
            r['artista'] = nombres_artistas[artista_limpio]
        else:
            coincidencia = next(
                (nombre_canon for clave, nombre_canon in nombres_artistas.items()
                 if artista_limpio in clave or clave in artista_limpio),
                None
            )
            if coincidencia:
                print(f"  CORREGIDO horarios: '{r['artista']}' → '{coincidencia}'")
                r['artista'] = coincidencia
            else:
                print(f"  SIN REFERENCIA horarios: artista '{r['artista']}' no en artistas.csv")
                inconsistencias.append(f"Artista sin referencia en horarios: '{r['artista']}'")

    escenarios_validos = set(MAPEO_ESCENARIOS.values())
    for r in horarios:
        if r.get('escenario') and r['escenario'] not in escenarios_validos:
            inconsistencias.append(f"Escenario desconocido en horarios: '{r['escenario']}'")

    print(f"\n  Total inconsistencias detectadas: {len(inconsistencias)}")
    return artistas, horarios, ventas, patrocinadores, inconsistencias

# ── FASE 10 ───────────────────────────────────────────────────────────────────

def fase10_exportacion(artistas, horarios, ventas, patrocinadores, auditorias, inconsistencias):
    print("\n" + "=" * 60)
    print("FASE 10: EXPORTACIÓN Y REPORTE FINAL")
    print("=" * 60)

    exportar_csv(artistas, os.path.join(LIMPIOS, 'artistas_limpio.csv'))
    exportar_csv(horarios, os.path.join(LIMPIOS, 'escenarios_horarios_limpio.csv'))
    exportar_csv(ventas, os.path.join(LIMPIOS, 'ventas_entradas_limpio.csv'))
    exportar_csv(patrocinadores, os.path.join(LIMPIOS, 'patrocinadores_limpio.csv'))

    exportar_excel(
        {
            'Artistas': artistas,
            'Horarios': horarios,
            'Ventas': ventas,
            'Patrocinadores': patrocinadores,
        },
        os.path.join(LIMPIOS, 'datos_completos.xlsx'),
    )

    informe = _generar_informe(artistas, horarios, ventas, patrocinadores, auditorias, inconsistencias)
    guardar_informe(informe, os.path.join(LIMPIOS, 'informe_limpieza.txt'))
    print("\n  Exportación completada.")

def _generar_informe(artistas, horarios, ventas, patrocinadores, auditorias, inconsistencias):
    aud_a, aud_h, aud_v, aud_p = auditorias
    hoy = date.today().strftime('%d/%m/%Y')
    orig_a = aud_a.get('total_registros', 0)
    orig_h = aud_h.get('total_registros', 0)
    orig_v = aud_v.get('total_registros', 0)
    orig_p = aud_p.get('total_registros', 0)
    total_orig = orig_a + orig_h + orig_v + orig_p
    total_final = len(artistas) + len(horarios) + len(ventas) + len(patrocinadores)

    lineas = [
        "=" * 60,
        "INFORME DE LIMPIEZA — FESTIVAL SOUNDWAVE 2026",
        f"Fecha del proceso: {hoy}",
        "=" * 60,
        "",
        "RESUMEN EJECUTIVO",
        "-" * 40,
        "Ficheros procesados: 4",
        f"Total registros originales: {total_orig}",
        f"Total registros finales:    {total_final}",
        "",
        "DETALLE POR FICHERO",
        "-" * 40,
        f"artistas.csv              {orig_a} → {len(artistas)} registros  (eliminados: {orig_a - len(artistas)})",
        f"escenarios_horarios.xlsx  {orig_h} → {len(horarios)} registros  (eliminados: {orig_h - len(horarios)})",
        f"ventas_entradas.json      {orig_v} → {len(ventas)} registros  (eliminados: {orig_v - len(ventas)})",
        f"patrocinadores.xml        {orig_p} → {len(patrocinadores)} registros  (eliminados: {orig_p - len(patrocinadores)})",
        "",
        "VALIDACIÓN CRUZADA",
        "-" * 40,
    ]
    if inconsistencias:
        lineas += [f"  - {inc}" for inc in inconsistencias]
    else:
        lineas.append("  Sin inconsistencias detectadas.")
    lineas += [
        "",
        "AVISOS",
        "-" * 40,
        "  Revisar manualmente campos marcados como 'REVISAR MANUALMENTE'.",
        "  Artistas sin referencia marcados como 'SIN REFERENCIA'.",
        "",
        "=" * 60,
        "FIN DEL INFORME",
        "=" * 60,
    ]
    return '\n'.join(lineas)

# ── PIPELINE ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    artistas, horarios, ventas, patrocinadores = fase1_carga()
    auditorias = fase2_auditoria(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase3_texto(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase4_tipos_y_vacios(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase5_categorias(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase6_fechas_y_horas(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase7_duplicados(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores = fase8_rangos(artistas, horarios, ventas, patrocinadores)
    artistas, horarios, ventas, patrocinadores, inconsistencias = fase9_validacion_cruzada(artistas, horarios, ventas, patrocinadores)
    fase10_exportacion(artistas, horarios, ventas, patrocinadores, auditorias, inconsistencias)
