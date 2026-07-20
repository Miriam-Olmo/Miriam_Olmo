from lib.limpieza import limpiar_texto, es_vacio


def auditar_fichero(datos, nombre):
    if not datos:
        print(f"\n=== AUDITORÍA: {nombre} === (sin datos)")
        return {}

    campos = list(datos[0].keys())
    vacios = {c: sum(1 for r in datos if es_vacio(r.get(c))) for c in campos}
    representaciones = [tuple(str(r.get(c, '')) for c in campos) for r in datos]
    duplicados = len(representaciones) - len(set(representaciones))
    espacios = {
        c: sum(1 for r in datos if r.get(c) is not None and str(r[c]) != str(r[c]).strip())
        for c in campos
    }

    print(f"\n=== AUDITORÍA: {nombre} ===")
    print(f"Total registros: {len(datos)}")
    print("Valores vacíos:")
    for c, n in vacios.items():
        if n:
            print(f"  - {c}: {n} vacíos")
    print(f"Duplicados exactos: {duplicados}")
    print("Espacios extra:")
    for c, n in espacios.items():
        if n:
            print(f"  - {c}: {n} con espacios")
    print("=" * 40)

    return {
        'total_registros': len(datos),
        'valores_vacios': vacios,
        'duplicados': duplicados,
        'espacios_extra': espacios,
    }


def detectar_fuera_de_rango(valor, minimo, maximo):
    if valor is None:
        return False
    try:
        return float(valor) < minimo or float(valor) > maximo
    except (TypeError, ValueError):
        return False


def eliminar_duplicados(datos, campos_clave):
    def clave(registro):
        return tuple(limpiar_texto(str(registro.get(c) or '')).lower() for c in campos_clave)

    def completitud(registro):
        return -sum(1 for v in registro.values() if es_vacio(v))

    vistos = {}
    for registro in datos:
        k = clave(registro)
        if k not in vistos or completitud(registro) > completitud(vistos[k]):
            vistos[k] = registro
    return list(vistos.values())
