def es_vacio_auditoria(valor):
    """Detecta de forma estricta si un valor está conceptualmente vacío en bruto."""
    if valor == None:
        return True
    cadena = str(valor).strip().lower()
    valores_nulos = ["", "n/a", "-", "no disponible", "vacio", "none", "undefined"]
    return cadena in valores_nulos


def calcular_vacios_por_columna(datos):
    """Cuenta cuántos valores vacíos existen por cada columna/campo."""
    if not datos:
        return {}
    
    # Inicializamos el diccionario de contadores con las columnas del primer registro
    columnas = datos[0].keys()
    contadores = {columna: 0 for columna in columnas}
    
    for registro in datos:
        for columna in columnas:
            if es_vacio_auditoria(registro.get(columna)):
                contadores[columna] += 1
                
    return contadores


def calcular_duplicados(datos, campos_clave):
    """Calcula cuántos registros repetidos existen según una clave combinada."""
    vistos = set()
    conteo_duplicados = 0
    for registro in datos:
        clave = tuple(str(registro.get(campo, "")).strip().lower() for campo in campos_clave)
        if clave in vistos:
            conteo_duplicados += 1
        vistos.add(clave)
    return conteo_duplicados


def auditar_fichero(nombre_fichero, datos, campos_clave, configuracion_anomalias=None):
    """Genera e imprime el informe estadístico de auditoría de calidad en consola."""
    print(f"\n📊 INFORME DE AUDITORÍA: {nombre_fichero.upper()}")
    print("=" * 50)
    print(f"Total registros analizados: {len(datos)}")
    
    if not datos:
        print("❌ Fichero vacío o sin registros para auditar.")
        print("=" * 50)
        return

    # Análisis de vacíos
    print("\n🔍 Valores Ausentes / Vacíos por Columna:")
    vacios = calcular_vacios_por_columna(datos)
    for columna, cantidad in vacios.items():
        porcentaje = (cantidad / len(datos)) * 100
        print(f" [{columna}]: {cantidad} vacíos ({porcentaje:.1f}%)")
        
    # Análisis de duplicados
    print("\n👥 Análisis de Duplicados:")
    total_duplicados = calcular_duplicados(datos, campos_clave)
    print(f"Registros repetidos basados en la clave {campos_clave}: {total_duplicados}")
    print('='*50)
    