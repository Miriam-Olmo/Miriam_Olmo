import os
from datetime import date

from lib.carga import cargar_csv, cargar_excel, cargar_json
from lib.limpieza import (
    aplicar_limpiar_texto, es_vacio, limpiar_texto,
    limpiar_valor_numerico, normalizar_categoria, normalizar_fecha,
)
from lib.auditoria import auditar_fichero, detectar_fuera_de_rango, eliminar_duplicados
from lib.exportacion import exportar_csv, exportar_excel, guardar_informe

DIR = os.path.dirname(__file__)
DATOS = os.path.join(DIR, 'datos')
LIMPIOS = os.path.join(DIR, 'datos_limpios')

# ── MAPPINGS ──────────────────────────────────────────────────────────────────

MAPEO_EQUIPOS = {
    'arctic foxes': 'Arctic Foxes', 'arctic fxoes': 'Arctic Foxes',
    'arcticfoxes': 'Arctic Foxes',
    'blaze team': 'Blaze Team', 'blazeteam': 'Blaze Team', 'blaze etam': 'Blaze Team',
    'byte force': 'Byte Force', 'byteforce': 'Byte Force', 'byet force': 'Byte Force',
    'crystal gaming': 'Crystal Gaming', 'crystalgaming': 'Crystal Gaming',
    'crystal gamnig': 'Crystal Gaming',
    'cyber dragons': 'Cyber Dragons', 'cyberdragons': 'Cyber Dragons',
    'cyberd ragons': 'Cyber Dragons',
    'dark wolves': 'Dark Wolves', 'darkwolves': 'Dark Wolves',
    'dar kwolves': 'Dark Wolves',
    'eclipse': 'Eclipse', 'eclpise': 'Eclipse',
    'iron bears': 'Iron Bears', 'ironbears': 'Iron Bears', 'iron baers': 'Iron Bears',
    'neon strikers': 'Neon Strikers', 'neonstrikers': 'Neon Strikers',
    'neon srtikers': 'Neon Strikers',
    'nova squad': 'Nova Squad', 'noav squad': 'Nova Squad', 'novasquad': 'Nova Squad',
    'omega team': 'Omega Team', 'omegateam': 'Omega Team', 'omgea team': 'Omega Team',
    'phoenix rising': 'Phoenix Rising', 'phoenixrising': 'Phoenix Rising',
    'phoenix risign': 'Phoenix Rising',
    'quantum five': 'Quantum Five', 'quantmu five': 'Quantum Five',
    'quantumfive': 'Quantum Five',
    'raptors gg': 'Raptors GG', 'raptorsgg': 'Raptors GG', 'ratpors gg': 'Raptors GG',
    'shadow legion': 'Shadow Legion', 'shadowlegion': 'Shadow Legion',
    'shado wlegion': 'Shadow Legion',
    'storm gaming': 'Storm Gaming', 'stormgaming': 'Storm Gaming',
    'stomr gaming': 'Storm Gaming',
    'thunder esports': 'Thunder Esports', 'thnuder esports': 'Thunder Esports',
    'thunderesports': 'Thunder Esports',
    'titan esports': 'Titan Esports', 'titanesports': 'Titan Esports',
    'tita nesports': 'Titan Esports',
    'vortex club': 'Vortex Club', 'vortexclub': 'Vortex Club', 'voretx club': 'Vortex Club',
    'zenith': 'Zenith', 'zeinth': 'Zenith',
}

MAPEO_ROLES = {
    'igl': 'IGL', 'in game leader': 'IGL', 'líder': 'IGL', 'lider': 'IGL',
    'awper': 'AWPer', 'sniper': 'AWPer',
    'entry': 'Entry', 'entry fragger': 'Entry', 'entrada': 'Entry',
    'support': 'Support', 'soporte': 'Support', 'sup': 'Support',
    'lurker': 'Lurker',
    'flex': 'Flex', 'flexible': 'Flex',
    'tank': 'Tank', 'tanque': 'Tank',
    'damage': 'DPS', 'dps': 'DPS',
}

MAPEO_PAISES = {
    'españa': 'España', 'espana': 'España', 'espña': 'España',
    'argentina': 'Argentina', 'argetina': 'Argentina',
    'brasil': 'Brasil', 'brazil': 'Brasil',
    'chile': 'Chile',
    'colombia': 'Colombia', 'kolombia': 'Colombia',
    'corea del sur': 'Corea del Sur', 'corea': 'Corea del Sur',
    'kr': 'Corea del Sur', 'korea': 'Corea del Sur',
    'dinamarca': 'Dinamarca', 'denmark': 'Dinamarca',
    'francia': 'Francia', 'france': 'Francia',
    'méxico': 'México', 'mexico': 'México', 'mejico': 'México',
    'perú': 'Perú', 'peru': 'Perú',
    'portugal': 'Portugal',
    'suecia': 'Suecia', 'sweden': 'Suecia',
}

MAPEO_REGIONES = {
    'europa': 'Europa', 'eu': 'Europa',
    'asia': 'Asia',
    'latinoamerica': 'Latinoamérica', 'latinoamérica': 'Latinoamérica', 'latam': 'Latinoamérica',
    'norteamerica': 'Norteamérica', 'norteamérica': 'Norteamérica',
}

MAPEO_CARGOS = {
    'coach': 'Coach', 'entrenador': 'Coach',
    'analista': 'Analista', 'analyst': 'Analista',
    'manager': 'Manager', 'mánager': 'Manager',
    'fisioterapeuta': 'Fisioterapeuta', 'fisio': 'Fisioterapeuta',
    'psicólogo deportivo': 'Psicólogo Deportivo',
    'psicologo deportivo': 'Psicólogo Deportivo',
    'psicólogo': 'Psicólogo Deportivo',
    'streamer oficial': 'Streamer Oficial',
}

MAPEO_MAPAS = {
    'mirage': 'Mirage', 'miraje': 'Mirage',
    'bind': 'Bind',
    'dust2': 'Dust2', 'dust 2': 'Dust2', 'dust_2': 'Dust2',
    'inferno': 'Inferno', 'infenro': 'Inferno',
    'haven': 'Haven', 'haeven': 'Haven',
    'ascent': 'Ascent', 'ascnet': 'Ascent',
    'vertigo': 'Vertigo', 'vértigo': 'Vertigo',
    'ancient': 'Ancient',
    'nuke': 'Nuke',
    'overpass': 'Overpass', 'overpas': 'Overpass', 'over pass': 'Overpass',
}

MAPEO_TORNEOS = {
    'cyberleague temporada 1': 'CyberLeague S1',
    'cyberleague s1': 'CyberLeague S1',
    'cyberleague season 1': 'CyberLeague S1',
    'cyber league s1': 'CyberLeague S1',
    'cyberleague temporada 2': 'CyberLeague S2',
    'cyberleague s2': 'CyberLeague S2',
    'cyber league s2': 'CyberLeague S2',
    'copa nacional': 'Copa Nacional', 'copa nac.': 'Copa Nacional',
    'grand finals': 'Grand Finals', 'gran final': 'Grand Finals',
    'grand final': 'Grand Finals',
    'masters series': 'Masters Series', 'master series': 'Masters Series',
    'masters': 'Masters Series',
    'open qualifier': 'Open Qualifier', 'open': 'Open Qualifier',
    'qualifier': 'Open Qualifier',
}

MAPEO_POSICIONES = {
    '1': '1', '1er': '1', '1º': '1', 'primero': '1', 'primer lugar': '1',
    '2': '2', '2do': '2', '2º': '2', 'segundo': '2', 'segundo lugar': '2',
    '3': '3', '3º': '3', 'tercero': '3', 'tercer lugar': '3',
    '4': '4', '4º': '4', 'cuarto': '4', 'cuarto lugar': '4',
    '5': '5', '5to': '5', '5º': '5', 'quinto': '5',
    '6': '6', '6to': '6', '6º': '6', 'sexto': '6',
    '7': '7', '7º': '7', 'séptimo': '7', 'septimo': '7',
    '8': '8', '8º': '8', 'octavo': '8',
}

# ── FASE 1 ────────────────────────────────────────────────────────────────────

def fase1_carga():
    print("\n" + "=" * 60)
    print("FASE 1: CARGA DE DATOS")
    print("=" * 60)

    jugadores = cargar_csv(os.path.join(DATOS, 'jugadores.csv'))
    equipos = cargar_excel(os.path.join(DATOS, 'equipos.xlsx'), hoja='equipos')
    staff = cargar_excel(os.path.join(DATOS, 'equipos.xlsx'), hoja='staff')
    partidas = cargar_json(os.path.join(DATOS, 'partidas.json'))
    premios = cargar_csv(os.path.join(DATOS, 'premios.csv'))

    for nombre, datos in [
        ('jugadores.csv', jugadores),
        ('equipos.xlsx [equipos]', equipos),
        ('equipos.xlsx [staff]', staff),
        ('partidas.json', partidas),
        ('premios.csv', premios),
    ]:
        print(f"\n--- {nombre} ---")
        print(f"  Registros: {len(datos)}")
        print(f"  Campos: {list(datos[0].keys()) if datos else []}")
        print("  Primeros 5 registros:")
        for r in datos[:5]:
            print(f"    {r}")

    return jugadores, equipos, staff, partidas, premios

# ── FASE 2 ────────────────────────────────────────────────────────────────────

def fase2_auditoria(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 2: AUDITORÍA DE CALIDAD")
    print("=" * 60)

    return (
        auditar_fichero(jugadores, 'jugadores.csv'),
        auditar_fichero(equipos, 'equipos.xlsx [equipos]'),
        auditar_fichero(staff, 'equipos.xlsx [staff]'),
        auditar_fichero(partidas, 'partidas.json'),
        auditar_fichero(premios, 'premios.csv'),
    )

# ── FASE 3 ────────────────────────────────────────────────────────────────────

def fase3_texto(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 3: LIMPIEZA DE TEXTO Y ESPACIOS")
    print("=" * 60)

    aplicar_limpiar_texto(jugadores,
        ['gamertag', 'nombre_real', 'pais', 'equipo', 'rol'],
        'jugadores.csv')
    aplicar_limpiar_texto(equipos,
        ['nombre_equipo', 'region', 'sede'],
        'equipos.xlsx [equipos]')
    aplicar_limpiar_texto(staff,
        ['equipo', 'nombre', 'cargo', 'email'],
        'equipos.xlsx [staff]')
    aplicar_limpiar_texto(partidas,
        ['equipo_1', 'equipo_2', 'mapa', 'torneo'],
        'partidas.json')
    aplicar_limpiar_texto(premios,
        ['torneo', 'equipo', 'posicion'],
        'premios.csv')

    return jugadores, equipos, staff, partidas, premios

# ── FASE 4 ────────────────────────────────────────────────────────────────────

def fase4_tipos_y_vacios(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 4: TIPOS Y VALORES VACÍOS")
    print("=" * 60)

    n = 0
    for r in jugadores:
        v = limpiar_valor_numerico(r.get('edad'))
        if v is not None:
            r['edad'] = v
            n += 1
        v2 = limpiar_valor_numerico(r.get('salario_mensual'))
        if v2 is not None:
            r['salario_mensual'] = v2
    print(f"  jugadores.csv > edad: {n} valores convertidos a número")

    n = 0
    for r in equipos:
        v = limpiar_valor_numerico(r.get('presupuesto_anual'))
        if v is not None:
            r['presupuesto_anual'] = v
            n += 1
        v2 = limpiar_valor_numerico(r.get('anio_fundacion'))
        if v2 is not None:
            r['anio_fundacion'] = v2
    print(f"  equipos.xlsx > presupuesto_anual: {n} valores convertidos a número")

    n = 0
    for r in partidas:
        for campo in ('puntuacion_1', 'puntuacion_2'):
            v = limpiar_valor_numerico(r.get(campo))
            if v is not None:
                r[campo] = v
        v = limpiar_valor_numerico(r.get('duracion_minutos'))
        if v is not None:
            r['duracion_minutos'] = v
            n += 1
        if es_vacio(r.get('mapa')):
            r['mapa'] = 'SIN DATOS'
    print(f"  partidas.json > duracion_minutos: {n} valores convertidos a número")

    n = 0
    for r in premios:
        v = limpiar_valor_numerico(r.get('premio_eur'))
        if v is not None:
            r['premio_eur'] = v
            n += 1
    print(f"  premios.csv > premio_eur: {n} valores convertidos a número")

    for r in staff:
        if es_vacio(r.get('email')):
            r['email'] = 'SIN DATOS'
        if es_vacio(r.get('telefono')):
            r['telefono'] = 'SIN DATOS'

    return jugadores, equipos, staff, partidas, premios

# ── FASE 5 ────────────────────────────────────────────────────────────────────

def fase5_categorias(jugadores, equipos, staff, partidas, premios):
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

    normalizar_campo(jugadores, 'equipo', MAPEO_EQUIPOS, 'jugadores.csv')
    normalizar_campo(jugadores, 'rol', MAPEO_ROLES, 'jugadores.csv')
    normalizar_campo(jugadores, 'pais', MAPEO_PAISES, 'jugadores.csv')
    normalizar_campo(equipos, 'nombre_equipo', MAPEO_EQUIPOS, 'equipos.xlsx [equipos]')
    normalizar_campo(equipos, 'region', MAPEO_REGIONES, 'equipos.xlsx [equipos]')
    normalizar_campo(staff, 'equipo', MAPEO_EQUIPOS, 'equipos.xlsx [staff]')
    normalizar_campo(staff, 'cargo', MAPEO_CARGOS, 'equipos.xlsx [staff]')
    normalizar_campo(partidas, 'equipo_1', MAPEO_EQUIPOS, 'partidas.json')
    normalizar_campo(partidas, 'equipo_2', MAPEO_EQUIPOS, 'partidas.json')
    normalizar_campo(partidas, 'mapa', MAPEO_MAPAS, 'partidas.json')
    normalizar_campo(partidas, 'torneo', MAPEO_TORNEOS, 'partidas.json')
    normalizar_campo(premios, 'equipo', MAPEO_EQUIPOS, 'premios.csv')
    normalizar_campo(premios, 'torneo', MAPEO_TORNEOS, 'premios.csv')
    normalizar_campo(premios, 'posicion', MAPEO_POSICIONES, 'premios.csv')

    return jugadores, equipos, staff, partidas, premios

# ── FASE 6 ────────────────────────────────────────────────────────────────────

def fase6_fechas(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 6: NORMALIZACIÓN DE FECHAS")
    print("=" * 60)

    def normalizar_campo_fecha(datos, campo, nombre):
        ok = err = 0
        for r in datos:
            v = r.get(campo)
            if v and not es_vacio(str(v)):
                nueva = normalizar_fecha(str(v))
                r[campo] = nueva
                if nueva == 'FECHA INVÁLIDA':
                    err += 1
                else:
                    ok += 1
        print(f"  {nombre} > {campo}: {ok} normalizadas, {err} inválidas")

    normalizar_campo_fecha(partidas, 'fecha', 'partidas.json')
    normalizar_campo_fecha(premios, 'fecha', 'premios.csv')

    return jugadores, equipos, staff, partidas, premios

# ── FASE 7 ────────────────────────────────────────────────────────────────────

def fase7_duplicados(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 7: ELIMINACIÓN DE DUPLICADOS")
    print("=" * 60)

    def dedup(datos, campos, nombre):
        antes = len(datos)
        datos = eliminar_duplicados(datos, campos)
        print(f"  {nombre}: {antes - len(datos)} duplicados eliminados ({antes} → {len(datos)} registros)")
        return datos

    jugadores = dedup(jugadores, ['gamertag'], 'jugadores.csv')
    equipos = dedup(equipos, ['nombre_equipo'], 'equipos.xlsx [equipos]')
    staff = dedup(staff, ['nombre', 'equipo'], 'equipos.xlsx [staff]')
    partidas = dedup(partidas, ['id_partida'], 'partidas.json')
    premios = dedup(premios, ['torneo', 'edicion', 'equipo'], 'premios.csv')

    return jugadores, equipos, staff, partidas, premios

# ── FASE 8 ────────────────────────────────────────────────────────────────────

def fase8_rangos(jugadores, equipos, staff, partidas, premios):
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

    corregir_rango(jugadores, 'edad', 14, 45, 'jugadores.csv')
    corregir_rango(jugadores, 'salario_mensual', 500, 50_000, 'jugadores.csv')
    corregir_rango(partidas, 'puntuacion_1', 0, 30, 'partidas.json')
    corregir_rango(partidas, 'puntuacion_2', 0, 30, 'partidas.json')
    corregir_rango(partidas, 'duracion_minutos', 5, 120, 'partidas.json')
    corregir_rango(premios, 'premio_eur', 100, 1_000_000, 'premios.csv')

    return jugadores, equipos, staff, partidas, premios

# ── FASE 9 ────────────────────────────────────────────────────────────────────

def fase9_validacion_cruzada(jugadores, equipos, staff, partidas, premios):
    print("\n" + "=" * 60)
    print("FASE 9: VALIDACIÓN CRUZADA")
    print("=" * 60)

    inconsistencias = []
    nombres_equipos = {limpiar_texto(r['nombre_equipo']).lower(): r['nombre_equipo'] for r in equipos}
    torneos_partidas = {limpiar_texto(r.get('torneo') or '').lower() for r in partidas}

    # Primero: detectar auto-enfrentamientos (antes de modificar campos)
    for r in partidas:
        eq1 = limpiar_texto(str(r.get('equipo_1') or '')).lower()
        eq2 = limpiar_texto(str(r.get('equipo_2') or '')).lower()
        if eq1 and eq1 == eq2:
            print(f"  INVÁLIDO partidas: {r.get('id_partida')} — equipo juega contra sí mismo ({r.get('equipo_1')})")
            inconsistencias.append(f"Partida {r.get('id_partida')}: equipo contra sí mismo ({r.get('equipo_1')})")

    def validar_equipo(datos, campo, nombre_fichero):
        for r in datos:
            eq = limpiar_texto(str(r.get(campo) or '')).lower()
            if not eq or eq in ('sin datos', 'sin referencia'):
                continue
            if eq not in nombres_equipos:
                print(f"  SIN REFERENCIA {nombre_fichero}: equipo '{r[campo]}' no en equipos.xlsx")
                inconsistencias.append(f"Equipo sin referencia en {nombre_fichero}: '{r[campo]}'")
                r[campo] = str(r[campo]) + ' [SIN REFERENCIA]'

    validar_equipo(jugadores, 'equipo', 'jugadores.csv')
    validar_equipo(partidas, 'equipo_1', 'partidas.json')
    validar_equipo(partidas, 'equipo_2', 'partidas.json')
    validar_equipo(premios, 'equipo', 'premios.csv')

    # Torneos en premios deben existir en partidas
    for r in premios:
        torneo = limpiar_texto(str(r.get('torneo') or '')).lower()
        if torneo and torneo not in torneos_partidas:
            inconsistencias.append(f"Torneo en premios sin partidas: '{r.get('torneo')}'")

    print(f"\n  Total inconsistencias detectadas: {len(inconsistencias)}")
    return jugadores, equipos, staff, partidas, premios, inconsistencias

# ── FASE 10 ───────────────────────────────────────────────────────────────────

def fase10_exportacion(jugadores, equipos, staff, partidas, premios, auditorias, inconsistencias):
    print("\n" + "=" * 60)
    print("FASE 10: EXPORTACIÓN Y REPORTE FINAL")
    print("=" * 60)

    exportar_csv(jugadores, os.path.join(LIMPIOS, 'jugadores_limpio.csv'))
    exportar_csv(equipos, os.path.join(LIMPIOS, 'equipos_limpio.csv'))
    exportar_csv(staff, os.path.join(LIMPIOS, 'staff_limpio.csv'))
    exportar_csv(partidas, os.path.join(LIMPIOS, 'partidas_limpio.csv'))
    exportar_csv(premios, os.path.join(LIMPIOS, 'premios_limpio.csv'))

    exportar_excel(
        {
            'Jugadores': jugadores,
            'Equipos': equipos,
            'Staff': staff,
            'Partidas': partidas,
            'Premios': premios,
        },
        os.path.join(LIMPIOS, 'datos_completos.xlsx'),
    )

    informe = _generar_informe(jugadores, equipos, staff, partidas, premios, auditorias, inconsistencias)
    guardar_informe(informe, os.path.join(LIMPIOS, 'informe_limpieza.txt'))
    print("\n  Exportación completada.")

def _generar_informe(jugadores, equipos, staff, partidas, premios, auditorias, inconsistencias):
    aud_j, aud_e, aud_s, aud_p, aud_pr = auditorias
    hoy = date.today().strftime('%d/%m/%Y')
    orig_j = aud_j.get('total_registros', 0)
    orig_e = aud_e.get('total_registros', 0)
    orig_s = aud_s.get('total_registros', 0)
    orig_p = aud_p.get('total_registros', 0)
    orig_pr = aud_pr.get('total_registros', 0)
    total_orig = orig_j + orig_e + orig_s + orig_p + orig_pr
    total_final = len(jugadores) + len(equipos) + len(staff) + len(partidas) + len(premios)

    lineas = [
        "=" * 60,
        "INFORME DE LIMPIEZA — CYBERLEAGUE PRO",
        f"Fecha del proceso: {hoy}",
        "=" * 60,
        "",
        "RESUMEN EJECUTIVO",
        "-" * 40,
        "Ficheros procesados: 5 (equipos.xlsx tiene 2 hojas)",
        f"Total registros originales: {total_orig}",
        f"Total registros finales:    {total_final}",
        "",
        "DETALLE POR FICHERO",
        "-" * 40,
        f"jugadores.csv             {orig_j} → {len(jugadores)} registros  (eliminados: {orig_j - len(jugadores)})",
        f"equipos.xlsx [equipos]    {orig_e} → {len(equipos)} registros  (eliminados: {orig_e - len(equipos)})",
        f"equipos.xlsx [staff]      {orig_s} → {len(staff)} registros  (eliminados: {orig_s - len(staff)})",
        f"partidas.json             {orig_p} → {len(partidas)} registros  (eliminados: {orig_p - len(partidas)})",
        f"premios.csv               {orig_pr} → {len(premios)} registros  (eliminados: {orig_pr - len(premios)})",
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
        "  Equipos sin referencia marcados como '[SIN REFERENCIA]'.",
        "",
        "=" * 60,
        "FIN DEL INFORME",
        "=" * 60,
    ]
    return '\n'.join(lineas)

# ── PIPELINE ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    jugadores, equipos, staff, partidas, premios = fase1_carga()
    auditorias = fase2_auditoria(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase3_texto(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase4_tipos_y_vacios(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase5_categorias(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase6_fechas(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase7_duplicados(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios = fase8_rangos(jugadores, equipos, staff, partidas, premios)
    jugadores, equipos, staff, partidas, premios, inconsistencias = fase9_validacion_cruzada(jugadores, equipos, staff, partidas, premios)
    fase10_exportacion(jugadores, equipos, staff, partidas, premios, auditorias, inconsistencias)
