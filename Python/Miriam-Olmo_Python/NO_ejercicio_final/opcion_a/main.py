import os
from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml
from lib.auditoria import auditar_fichero
from lib.limpieza import (
    normalizar_texto,
    limpiar_valor_numerico,
    normalizar_categoria,
    normalizar_fecha,
    eliminar_duplicados,
    mapeos_categorias
)
from lib.exportacion import crear_csv, crear_excel_completo, crear_informe_txt

# ------------------------------------------------------------------------------
# 1. FUNCIONES PEQUEÑAS DE LIMPIEZA ESPECÍFICA (SIN ABREVIATURAS)
# ------------------------------------------------------------------------------

def limpiar_registro_artista(registro_bruto):
    """Aplica la limpieza específica columna por columna para los artistas."""
    registro_limpio = {}
    contador_valores_vacios = 0
    
    # Procesar Nombre Artista (Texto General)
    nombre_artista = registro_bruto.get("nombre_artista")
    nombre_normalizado = normalizar_texto(nombre_artista) if nombre_artista is not None else ""
    registro_limpio["nombre_artista"] = nombre_normalizado if nombre_normalizado != "" else "SIN DATOS"
    if nombre_normalizado == "": 
        contador_valores_vacios += 1
    
    # Procesar Género Musical (Categoría Guiada)
    genero_bruto = registro_bruto.get("genero")
    diccionario_mapeo_genero = mapeos_categorias.get("genero_musical")
    registro_limpio["genero"] = normalizar_categoria(genero_bruto, diccionario_mapeo_genero, "genero")
    if registro_limpio["genero"] == "SIN DATOS": 
        contador_valores_vacios += 1
    
    # Procesar Caché (Numérico Monetario)
    cache_bruto = registro_bruto.get("cache")
    cache_limpio = limpiar_valor_numerico(cache_bruto)
    registro_limpio["cache"] = cache_limpio if cache_limpio is not None else 0
    if cache_limpio is None: 
        contador_valores_vacios += 1
    
    return registro_limpio, contador_valores_vacios


def limpiar_registro_programa(registro_bruto):
    """Aplica la limpieza específica columna por columna para escenarios y horarios."""
    registro_limpio = {}
    contador_valores_vacios = 0
    
    # Escenario (Texto General)
    escenario_bruto = registro_bruto.get("escenario")
    escenario_normalizado = normalizar_texto(escenario_bruto) if escenario_bruto is not None else ""
    registro_limpio["escenario"] = escenario_normalizado if escenario_normalizado != "" else "SIN DATOS"
    if escenario_normalizado == "": 
        contador_valores_vacios += 1
        
    # Hora Inicio (Texto General)
    hora_bruta = registro_bruto.get("hora_inicio")
    hora_normalizada = normalizar_texto(hora_bruta) if hora_bruta is not None else ""
    registro_limpio["hora_inicio"] = hora_normalizada if hora_normalizada != "" else "SIN DATOS"
    if hora_normalizada == "": 
        contador_valores_vacios += 1
    
    # Artista Confirmado (Texto General)
    artista_bruto = registro_bruto.get("artista_confirmado")
    artista_normalizado = normalizar_texto(artista_bruto) if artista_bruto is not None else ""
    registro_limpio["artista_confirmado"] = artista_normalizado if artista_normalizado != "" else "SIN DATOS"
    if artista_normalizado == "": 
        contador_valores_vacios += 1
    
    return registro_limpio, contador_valores_vacios


def limpiar_registro_patrocinador(registro_bruto):
    """Aplica la limpieza específica columna por columna para los patrocinadores."""
    registro_limpio = {}
    contador_valores_vacios = 0
    
    # Campos de Texto Base
    empresa_bruta = registro_bruto.get("nombre_empresa")
    contacto_bruto = registro_bruto.get("contacto")
    email_bruto = registro_bruto.get("email")
    
    empresa_normalizada = normalizar_texto(empresa_bruta) if empresa_bruta is not None else ""
    contacto_normalizado = normalizar_texto(contacto_bruto) if contacto_bruto is not None else ""
    email_normalizado = normalizar_texto(email_bruto) if email_bruto is not None else ""
    
    registro_limpio["nombre_empresa"] = empresa_normalizada if empresa_normalizada != "" else "SIN DATOS"
    registro_limpio["contacto"] = contacto_normalizado if contacto_normalizado != "" else "SIN DATOS"
    registro_limpio["email"] = email_normalizado if email_normalizado != "" else "SIN DATOS"
    
    if empresa_normalizada == "": contador_valores_vacios += 1
    if contacto_normalizado == "": contador_valores_vacios += 1
    if email_normalizado == "": contador_valores_vacios += 1
    
    # Importe Patrocinio (Numérico Monetario)
    importe_bruto = registro_bruto.get("importe_patrocinio")
    importe_limpio = limpiar_valor_numerico(importe_bruto)
    registro_limpio["importe_patrocinio"] = importe_limpio if importe_limpio is not None else 0
    if importe_limpio is None: 
        contador_valores_vacios += 1
    
    # Categoría de Patrocinio (Categoría Guiada)
    categoria_bruta = registro_bruto.get("categoria")
    
    # Se usa la clave exacta de tu módulo limpieza.py: 'categoria_patrocinio'
    diccionario_mapeo_patrocinio = mapeos_categorias.get("categoria_patrocinio")
    
    # Control de seguridad en caso de que el diccionario no se cargue correctamente
    if diccionario_mapeo_patrocinio is None:
        diccionario_mapeo_patrocinio = {}
        
    registro_limpio["categoria"] = normalizar_categoria(categoria_bruta, diccionario_mapeo_patrocinio, "categoria")
    if registro_limpio["categoria"] == "SIN DATOS": 
        contador_valores_vacios += 1
    
    return registro_limpio, contador_valores_vacios


def limpiar_registro_venta(registro_bruto):
    """Aplica la limpieza específica columna por columna para las ventas de entradas."""
    registro_limpio = {}
    contador_valores_vacios = 0
    
    # Identificador de entrada (Texto General)
    id_entrada_bruto = registro_bruto.get("id_entrada")
    id_entrada_normalizado = normalizar_texto(id_entrada_bruto) if id_entrada_bruto is not None else ""
    registro_limpio["id_entrada"] = id_entrada_normalizado if id_entrada_normalizado != "" else "SIN DATOS"
    if id_entrada_normalizado == "": 
        contador_valores_vacios += 1
    
    # Tipo Entrada y Método Pago (Texto General)
    tipo_entrada_bruto = registro_bruto.get("tipo_entrada")
    metodo_pago_bruto = registro_bruto.get("metodo_pago")
    
    tipo_normalizado = normalizar_texto(tipo_entrada_bruto) if tipo_entrada_bruto is not None else ""
    metodo_normalizado = normalizar_texto(metodo_pago_bruto) if metodo_pago_bruto is not None else ""
    
    # Convertimos los valores normalizados
    registro_limpio["tipo_entrada"] = tipo_normalizado if tipo_normalizado != "" else "SIN DATOS"
    registro_limpio["metodo_pago"] = metodo_normalizado if metodo_normalizado != "" else "SIN DATOS"
    
    if tipo_normalizado == "": contador_valores_vacios += 1
    if metodo_normalizado == "": contador_valores_vacios += 1
    
    # Precio y Cantidad (Numéricos)
    precio_bruto = registro_bruto.get("precio")
    cantidad_bruta = registro_bruto.get("cantidad")
    
    precio_limpio = limpiar_valor_numerico(precio_bruto)
    cantidad_limpia = limpiar_valor_numerico(cantidad_bruta)
    
    registro_limpio["precio"] = precio_limpio if precio_limpio is not None else 0
    registro_limpio["cantidad"] = cantidad_limpia if cantidad_limpia is not None else 0
    
    if precio_limpio is None: contador_valores_vacios += 1
    if cantidad_limpia is None: contador_valores_vacios += 1
    
    # Campo de Fecha (Conversión Multiformato)
    fecha_bruta = registro_bruto.get("fecha_compra")
    registro_limpio["fecha_compra"] = normalizar_fecha(fecha_bruta)
    if registro_limpio["fecha_compra"] == "FECHA INVÁLIDA": 
        contador_valores_vacios += 1
    
    return registro_limpio, contador_valores_vacios

# ------------------------------------------------------------------------------
# 2. FUNCIONES DE PROCESAMIENTO EN BUCLE (COLECCIONES)
# ------------------------------------------------------------------------------

def procesar_fichero_completo(lista_datos_brutos, funcion_limpieza_individual):
    """Aplica la función de transformación a toda una lista de registros en memoria."""
    lista_transformada = []
    total_vacios_tratados = 0
    
    for registro in lista_datos_brutos:
        registro_limpio, vacios_registro = funcion_limpieza_individual(registro)
        lista_transformada.append(registro_limpio)
        total_vacios_tratados += vacios_registro
        
    return lista_transformada, total_vacios_tratados


def obtener_conteo_fechas_y_categorias(lista_final, columna_categoria, nombre_campo_fecha):
    """Cuenta cuántas fechas válidas y categorías se han estructurado correctamente."""
    contador_categorias = 0
    contador_fechas = 0
    
    for registro in lista_final:
        if columna_categoria and registro.get(columna_categoria) not in ["SIN DATOS", None]:
            contador_categorias += 1
        if nombre_campo_fecha and registro.get(nombre_campo_fecha) not in ["FECHA INVÁLIDA", None]:
            contador_fechas += 1
            
    return contador_categorias, contador_fechas

# ------------------------------------------------------------------------------
# 3. ORQUESTADOR PRINCIPAL
# ------------------------------------------------------------------------------

def main():
    print("==== INICIANDO PIPELINE DE DATOS SOUNDWAVE 2026 ====\n")
    
    # FASE 1: Ingesta y Carga de ficheros a memoria desde la carpeta 'datos/'
    try:
        lista_artistas = cargar_csv('datos/artistas.csv')
        lista_programa = cargar_excel('datos/escenarios_horarios.xlsx')
        lista_patrocinadores = cargar_xml('datos/patrocinadores.xml')
        lista_ventas = cargar_json('datos/ventas_entradas.json')
        print("✔ ¡Todos los ficheros cargados correctamente en memoria!\n")
    except Exception as error_de_carga:
        print(f"❌ Error crítico al cargar los archivos iniciales: {error_de_carga}")
        return
    
    # FASE 2: Auditoría de calidad inicial sobre los datos en bruto en consola
    auditar_fichero("artistas", lista_artistas, ["nombre_artista"])
    auditar_fichero("escenarios_horarios", lista_programa, ["escenario", "hora_inicio"])
    auditar_fichero("patrocinadores", lista_patrocinadores, ["nombre_empresa"])
    auditar_fichero("ventas_entradas", lista_ventas, ["id_entrada"])

    datos_limpios_globales = {}
    metricas_para_informe = {}

    print("\n🧼 Aplicando transformaciones modulares específicas...")

    # --- PROCESAMIENTO FICHERO 1: ARTISTAS ---
    transformados_artistas, vacios_artistas = procesar_fichero_completo(lista_artistas, limpiar_registro_artista)
    finales_artistas, duplicados_artistas = eliminar_duplicados(transformados_artistas, ["nombre_artista"])
    datos_limpios_globales["artistas.csv"] = finales_artistas
    cat_artistas, fch_artistas = obtener_conteo_fechas_y_categorias(finales_artistas, "genero", None)
    metricas_para_informe["artistas.csv"] = {
        "originales": len(lista_artistas), "finales": len(finales_artistas), "duplicados": duplicados_artistas,
        "vacios": vacios_artistas, "categorias": cat_artistas, "fechas": fch_artistas
    }

    # --- PROCESAMIENTO FICHERO 2: ESCENARIOS HORARIOS ---
    transformados_programa, vacios_programa = procesar_fichero_completo(lista_programa, limpiar_registro_programa)
    finales_programa, duplicados_programa = eliminar_duplicados(transformados_programa, ["escenario", "hora_inicio"])
    datos_limpios_globales["escenarios_horarios.xlsx"] = finales_programa
    cat_programa, fch_programa = obtener_conteo_fechas_y_categorias(finales_programa, None, None)
    metricas_para_informe["escenarios_horarios.xlsx"] = {
        "originales": len(lista_programa), "finales": len(finales_programa), "duplicados": duplicados_programa,
        "vacios": vacios_programa, "categorias": cat_programa, "fechas": fch_programa
    }

    # --- PROCESAMIENTO FICHERO 3: PATROCINADORES ---
    transformados_patrocinadores, vacios_patrocinadores = procesar_fichero_completo(lista_patrocinadores, limpiar_registro_patrocinador)
    finales_patrocinadores, duplicados_patrocinadores = eliminar_duplicados(transformados_patrocinadores, ["nombre_empresa"])
    datos_limpios_globales["patrocinadores.xml"] = finales_patrocinadores
    cat_patrocinadores, fch_patrocinadores = obtener_conteo_fechas_y_categorias(finales_patrocinadores, "categoria", None)
    metricas_para_informe["patrocinadores.xml"] = {
        "originales": len(lista_patrocinadores), "finales": len(finales_patrocinadores), "duplicados": duplicados_patrocinadores,
        "vacios": vacios_patrocinadores, "categorias": cat_patrocinadores, "fechas": fch_patrocinadores
    }

    # --- PROCESAMIENTO FICHERO 4: VENTAS ENTRADAS ---
    transformados_ventas, vacios_ventas = procesar_fichero_completo(lista_ventas, limpiar_registro_venta)
    finales_ventas, duplicados_ventas = eliminar_duplicados(transformados_ventas, ["id_entrada"])
    datos_limpios_globales["ventas_entradas.json"] = finales_ventas
    cat_ventas, fch_ventas = obtener_conteo_fechas_y_categorias(finales_ventas, None, "fecha_compra")
    metricas_para_informe["ventas_entradas.json"] = {
        "originales": len(lista_ventas), "finales": len(finales_ventas), "duplicados": duplicados_ventas,
        "vacios": vacios_ventas, "categorias": cat_ventas, "fechas": fch_ventas
    }

    # FASE 10: Persistencia y almacenamiento de los resultados generados en disco
    carpeta_salida = 'datos_limpios'

    # Escritura individualizada en formato CSV limpio dentro de 'datos_limpios/'
    crear_csv(datos_limpios_globales["artistas.csv"], 'artistas_limpio.csv', carpeta_salida)
    crear_csv(datos_limpios_globales["escenarios_horarios.xlsx"], 'escenarios_horarios_limpio.csv', carpeta_salida)
    crear_csv(datos_limpios_globales["patrocinadores.xml"], 'patrocinadores_limpio.csv', carpeta_salida)
    crear_csv(datos_limpios_globales["ventas_entradas.json"], 'ventas_entradas_limpio.csv', carpeta_salida)

    # Mapeo estructurado para la generación del Libro de Excel Maestro Unificado
    diccionario_excel = {
        'artistas_limpios': datos_limpios_globales["artistas.csv"],
        'escenarios_horarios_limpios': datos_limpios_globales["escenarios_horarios.xlsx"],
        'patrocinadores_limpios': datos_limpios_globales["patrocinadores.xml"],
        'ventas_entradas_limpias': datos_limpios_globales["ventas_entradas.json"]
    }
    crear_excel_completo(diccionario_excel, carpeta_salida, "datos_completos")
    
    # Generación y almacenamiento del reporte final plano 'informe_limpieza.txt'
    crear_informe_txt(carpeta_salida, metricas_para_informe)
    
    print(f"\n🚀 Pipeline finalizado con éxito. Los registros limpios y completos están en: './{carpeta_salida}'")


if __name__ == "__main__":
    main()