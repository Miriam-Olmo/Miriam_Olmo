

# --- SECCIÓN DE IMPORTACIONES DE MÓDULOS PROPIOS (ARQUITECTURA MODULAR) ---
# Desde el paquete auxiliar lib, importamos las funciones encargadas de leer los datos en bruto (Fase de Extracción - E)
from lib.carga import cargar_csv, cargar_excel, cargar_json, cargar_xml

# Importamos todas las herramientas atómicas de limpieza y normalización semántica (Fase de Transformación - T)
from lib.limpieza import (
    limpiar_espacios, es_valor_vacio, corregir_palabra_tilde, normalizar_texto,
    normalizar_pais, normalizar_categoria, limpiar_simbolos_moneda, 
    unificar_separadores_decimales, limpiar_valor_numerico, limpiar_id, 
    limpiar_dni, normalizar_fecha, contar_vacios, eliminar_duplicados, mapeo_categoria
)

# Importamos la función de diagnóstico preliminar encargada de analizar la calidad del dato antes de limpiarlo
from lib.auditoria import auditar_fichero

# Importamos las rutinas encargadas de escribir y persistir los resultados en el almacenamiento (Fase de Carga - L)
from lib.exportacion import crear_csv, crear_excel_completo, crear_informe_txt


# ------------------------------------------------------------------------------
# FUNCIONES INTERMEDIAS PARA PROCESAR Y CORREGIR FILA POR FICHERO (TODAS LAS COLUMNAS)
# ------------------------------------------------------------------------------

def limpiar_lista_artistas(lista_artistas):
    """Itera sobre la lista de artistas aplicando transformaciones específicas columna por columna."""
    # Inicializa una lista vacía para almacenar los registros una vez estén sanitizados
    artistas_procesados = []
    # Accedemos de forma segura al sub-diccionario interno de géneros musicales definido en limpieza.py
    mapeo_generos = mapeo_categoria.get("genero_musical", {})
    
    # Bucle secuencial para recorrer cada artista (diccionario) de la colección original
    for registro in lista_artistas:
        # Creamos un diccionario vacío para volcar los pares clave-valor ya limpios
        copia_registro = {}
        # Recorremos el registro original limpiando espacios invisibles que puedan venir en los nombres de las columnas
        for clave, valor in registro.items():
            copia_registro[str(clave).strip()] = valor

        # --- Transformación de la columna 'id_artista' ---
        if "id_artista" in copia_registro:
            # Pasa el código identificador a minúsculas y retira espacios (ej: 'ART-01 ' -> 'art-01')
            copia_registro["id_artista"] = limpiar_id(copia_registro["id_artista"])
            
        # --- Transformación de la columna 'nombre_artista' ---
        if "nombre" in copia_registro: 
            # Reestablece espacios intermedios y capitaliza nombres/apellidos aplicando tildes del maestro
            copia_registro["nombre"] = normalizar_texto(copia_registro["nombre"])

        # --- Transformación de la columna 'genero_musical' ---
        if "genero_musical" in copia_registro: 
            # Cruza el valor con el diccionario de estilos musicales para estandarizar etiquetas (ej: 'rokc' -> 'Rock')
            copia_registro["genero_musical"] = normalizar_categoria(copia_registro["genero_musical"], mapeo_generos, "genero_musical")
            
        # --- Transformación de la columna 'pais_origen' ---
        if "pais" in copia_registro:
            # Estandariza las variantes idiomáticas o siglas de países usando el mapeo de naciones
            copia_registro["pais"] = normalizar_pais(copia_registro["pais"])
            
        # --- Transformación de la columna 'cache' (Caché económico) ---
        if "cache_eur" in copia_registro:
            # Remueve símbolos (€, $), unifica comas/puntos y transforma la celda en un dato numérico float puro
            copia_registro["cache_eur"] = limpiar_valor_numerico,(copia_registro["cache_eur"])
            
        # Incorpora el diccionario completamente transformado a la lista de resultados
        artistas_procesados.append(copia_registro)
        
    # Retorna la nueva colección de artistas completamente normalizada
    return artistas_procesados


def limpiar_lista_programa(lista_programa):
    """Itera sobre los horarios y escenarios del festival aplicando reglas de negocio."""
    programa_procesado = []
    mapeo_escenarios = mapeo_categoria.get("escenario", {})
    
    for registro in lista_programa:
        # CONSERVADO: Tu inicialización de diccionario y limpieza de espacios en las cabeceras
        copia_registro = {}
        for clave, valor in registro.items():
            copia_registro[str(clave).strip()] = valor

        # --- Transformación de la columna 'fecha' (Clave foránea de unión) ---
        if "fecha" in copia_registro:
            # CORREGIDO: Se almacena en la clave correspondiente para no destruir el objeto diccionario
            copia_registro["fecha"] = normalizar_fecha(copia_registro["fecha"])
            
        if "escenario" in copia_registro:
            copia_registro["escenario"] = normalizar_categoria(copia_registro["escenario"], mapeo_escenarios, "escenario")
            
        if 'artista' in copia_registro:
            copia_registro['artista'] = normalizar_texto(copia_registro['artista'])
            
        if "hora_inicio" in copia_registro:
            copia_registro["hora_inicio"] = limpiar_espacios(copia_registro["hora_inicio"])
            
        if "hora_fin" in copia_registro:
            copia_registro["hora_fin"] = limpiar_espacios(copia_registro["hora_fin"])
            
        if 'soundcheck' in copia_registro:
            copia_registro['soundcheck'] = normalizar_texto(copia_registro['soundcheck'])
            
        # --- Transformación de la columna 'notes' (Notas adicionales) ---
        if 'notes' in copia_registro:
            # CORREGIDO: Se accede a 'notes' (llave de origen) y se vuelca el resultado limpio en 'notas'
            copia_registro['notas'] = normalizar_texto(copia_registro['notes'])
            # Eliminamos la columna vieja en inglés para que la fila guardada quede perfecta
            if 'notes' != 'notas':
                copia_registro.pop('notes', None)
            
        programa_procesado.append(copia_registro)
        
    return programa_procesado


def limpiar_lista_patrocinadores(lista_patrocinadores):
    """Itera sobre las empresas patrocinadoras resolviendo la calidad de sus datos comerciales."""
    # Le indicamos a Python que busque 'mapeo_categoria' fuera de la función
    global mapeo_categoria
    # Inicializa la lista destino para las empresas analizadas
    patrocinadores_procesados = []
    # Recupera del módulo de limpieza el diccionario maestro de rangos de patrocinio
    mapeo_categoria = mapeo_categoria.get("categoria", {})
    
    # Recorre cada entidad extraída del árbol XML original
    for registro in lista_patrocinadores:
        copia_registro = {}
        for clave, valor in registro.items():
            copia_registro[str(clave).strip()] = valor

        # --- Transformación de la columna 'nombre_empresa' ---
        if "nombre_empresa" in copia_registro:
            copia_registro["nombre_empresa"] = normalizar_texto(copia_registro["nombre_empresa"])
            
        # --- Transformación de la columna 'contacto' (Nombre del agente corporativo) ---
        if "contacto" in copia_registro:
            copia_registro["contacto"] = normalizar_texto(copia_registro["contacto"])
            
        # --- Transformación de la columna 'email' ---
        if "email" in copia_registro:
            # Aplica una limpieza básica de caracteres y fuerza minúsculas estricta para correos electrónicos
            copia_registro["email"] = str(copia_registro["email"]).strip().lower() if copia_registro["email"] else "SIN DATOS"

        # --- Transformación de la columna 'importe_patrocinio' (Aportación financiera) ---
        if "importe_patrocinio" in copia_registro:
            copia_registro["importe_patrocinio"] = limpiar_valor_numerico(copia_registro["importe_patrocinio"])            

        # --- Transformación de la columna 'categoria' ---
        if "categoria" in copia_registro:
            # Valida el nivel estratégico del partner (ej: 'main sponsor' -> 'Principal')
            copia_registro["categoria"] = normalizar_categoria(copia_registro["categoria"], mapeo_categoria, "categoria")
        if 'fecha_inicio' in copia_registro:
            copia_registro['fecha_inicio'] = normalizar_fecha(copia_registro['fecha_inicio'])
        if 'fecha_fin' in copia_registro:
            copia_registro['fecha_fin'] = normalizar_fecha(copia_registro['fecha_fin'])
            

            
        # Consolida el patrocinador limpio en la lista de salida
        patrocinadores_procesados.append(copia_registro)
        
    return patrocinadores_procesados

def limpiar_lista_ventas(lista_ventas):
    """Itera sobre el registro de transacciones de la ticketera unificando formatos de cobro."""
    # Inicializa la lista receptora para la auditoría financiera de entradas
    ventas_procesadas = []
    # Extrae las equivalencias de tipos de pases y pasarelas de pago desde limpieza.py
    mapeo_tickets = mapeo_categoria.get("tipo_entrada", {})
    mapeo_pagos = mapeo_categoria.get("metodo_pago", {})
    
    # Recorre cada transacción de compra extraída del flujo JSON
    for registro in lista_ventas:
        copia_registro = {}
        for clave, valor in registro.items():
            copia_registro[str(clave).strip()] = valor

        # --- Transformación de la columna 'id_entrada' (Código único de ticket) ---
        if "id" in copia_registro:
            copia_registro["id"] = limpiar_id(copia_registro["id"])
            
        # --- Transformación de la columna 'id_artista' (Referencia al artista principal que van a ver) ---
        if "artista" in copia_registro:
            copia_registro["i" \
            "artista"] = limpiar_id(copia_registro["artista"])
            
        # --- Transformación de la columna 'dni_comprador' ---
        if "dni" in copia_registro:
            # Aplica el algoritmo de formateo con ceros a la izquierda y valida los componentes del DNI/NIE
            copia_registro["dni"] = limpiar_dni(copia_registro["dni"])
            
        # --- Transformación de la columna 'nombre_comprador' ---
        if "nombre" in copia_registro:
            copia_registro["nombre_comprador"] = normalizar_texto(copia_registro["nombre"])
            
        # --- Transformación de la columna 'tipo_entrada' ---
        if "tipo_entrada" in copia_registro:
            copia_registro["tipo_entrada"] = normalizar_categoria(copia_registro["tipo_entrada"], mapeo_tickets, "tipo_entrada")
            
        # --- Transformación de la columna 'precio_entrada' ---
        if "precio" in copia_registro:
        
            copia_registro["precio"] = limpiar_valor_numerico(copia_registro["precio"])
            
        # --- Transformación de la columna 'fecha_compra' ---
        if "fecha_compra" in copia_registro:
            # Enruta el texto hacia los analizadores heurísticos para unificarlo a formato 'DD/MM/AAAA'
            copia_registro["fecha_compra"] = normalizar_fecha(copia_registro["fecha_compra"])
            
        # --- Transformación de la columna 'metodo_pago' ---
        if "metodo_pago" in copia_registro:
            copia_registro["metodo_pago"] = normalizar_categoria(copia_registro["metodo_pago"], mapeo_pagos, "metodo_pago")
            
        # Guarda la venta auditada y estructurada
        ventas_procesadas.append(copia_registro)
        
    return ventas_procesadas

# ------------------------------------------------------------------------------
# FLUJO PRINCIPAL DE EJECUCIÓN (ENTRY POINT DEL PIPELINE ETL)
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Condicional que asegura que el script solo se ejecute al ser invocado directamente por terminal
    print("🚀 Iniciando el Pipeline ETL - Festival SoundWave 2026...")

    # ==========================================================================
    # FASE 1: EXTRAER (LOAD DESDE RECURSOS HETEROGÉNEOS)
    # ==========================================================================
    # Invoca las funciones del módulo carga.py apuntando a las rutas físicas de los datos fuente
    artistas_raw = cargar_csv("datos/artistas.csv")

    programa_raw = cargar_excel("datos/escenarios_horarios.xlsx")
    ventas_raw = cargar_json("datos/ventas_entradas.json")
    patrocinadores_raw = cargar_xml("datos/patrocinadores.xml")
    print("✔ Fase de Extracción finalizada con éxito.")

    # ==========================================================================
    # FASE 2: AUDITORÍA PRELIMINAR (DIAGNÓSTICO ESTADÍSTICO EN BRUTO)
    # ==========================================================================
    # Llama a auditar_fichero para exponer el volumen de nulos y duplicados iniciales en consola
    auditar_fichero("artistas.csv", artistas_raw, ["id_artista"])
    auditar_fichero("escenarios_horarios.xlsx", programa_raw, ["escenario", "hora_inicio"])
    auditar_fichero("patrocinadores.xml", patrocinadores_raw, ["nombre_empresa"])
    auditar_fichero("ventas_entradas.json", ventas_raw, ["id_venta"])

    # ==========================================================================
    # FASE 3: TRANSFORMACIÓN COLUMNA A COLUMNA (NORMALIZACIÓN SEMÁNTICA)
    # ==========================================================================
    # Envía los datos en bruto a las funciones intermedias para aplicar las reglas de negocio atómicas
    artistas_normalizados = limpiar_lista_artistas(artistas_raw)

    programa_normalizado = limpiar_lista_programa(programa_raw)
    patrocinadores_normalizados = limpiar_lista_patrocinadores(patrocinadores_raw)
    ventas_normalizadas = limpiar_lista_ventas(ventas_raw)
    print("✔ Fase de Normalización de contenido finalizada.")

    # ==========================================================================
    # FASE 4: INTEGRIDAD LÓGICA Y DEDUPLICACIÓN INTELIGENTE
    # ==========================================================================
    # Elimina los registros repetidos basándose en claves lógicas compuestas, reteniendo la fila más completa
    artistas_limpios, duplicados_artistas = eliminar_duplicados(artistas_normalizados, ["id_artista"])
    programa_limpio, duplicados_programa = eliminar_duplicados(programa_normalizado, ["escenario", "hora_inicio"])
    patrocinadores_limpios, duplicados_patrocinadores = eliminar_duplicados(patrocinadores_normalizados, ["nombre_empresa"])
    ventas_limpias, duplicados_ventas = eliminar_duplicados(ventas_normalizadas, ["id_venta"])
    print("✔ Limpieza de duplicados e integridad completada de forma estricta.")

    # ==========================================================================
    # FASE 5: CARGA / VOLCADO (PERSISTENCIA MULTIFORMATO)
    # ==========================================================================
    # Define la constante con el nombre del directorio donde se almacenarán las estructuras limpias
    carpeta_salida = 'datos_limpios'

    # 1. Escritura de archivos CSV individuales e independientes de cada entidad refinada
    crear_csv(artistas_limpios, 'artistas_limpio.csv', carpeta_salida)
    crear_csv(programa_limpio, 'escenarios_horarios_limpio.csv', carpeta_salida)
    crear_csv(patrocinadores_limpios, 'patrocinadores_limpio.csv', carpeta_salida)
    crear_csv(ventas_limpias, 'ventas_entradas_limpio.csv', carpeta_salida)

    # 2. Estructuración del diccionario unificado de datos para la generación del reporte consolidado
    datos_excel = {
        'artistas_limpios': artistas_limpios,
        'escenarios_horarios_limpios': programa_limpio,
        'patrocinadores_limpios': patrocinadores_limpios,
        'ventas_entradas_limpias': ventas_limpias
    }
    
    # Crea el libro binario de Excel (.xlsx) mapeando cada clave del diccionario como una pestaña independiente
    crear_excel_completo(datos_excel, carpeta_salida, 'datos_completos')

    # 3. Generación automática en disco del informe estático TXT exigido con las métricas finales del proceso
    crear_informe_txt(carpeta_salida, 'informe_limpieza.txt')

    print("\n🏁 ¡Proceso ETL completado con éxito! Los datos limpios están listos para explotación.")