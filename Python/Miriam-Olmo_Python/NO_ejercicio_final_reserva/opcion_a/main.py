# ============================================
# MAIN.PY
# ============================================

from lib.carga import cargar_csv
from lib.carga import cargar_excel
from lib.carga import cargar_json
from lib.carga import cargar_xml

from lib.auditoria import auditar_datos

from lib.limpieza import normalizar_texto
from lib.limpieza import normalizar_categoria
from lib.limpieza import limpiar_valor_numerico
from lib.limpieza import normalizar_fecha
from lib.limpieza import eliminar_duplicados

from lib.exportacion import exportar_csv
from lib.exportacion import exportar_excel
from lib.exportacion import guardar_informe

# ============================================
# LIMPIAR ARTISTAS
# ============================================

def limpiar_artistas(
    lista_artistas
):

    for artista in lista_artistas:

        if "nombre" in artista:

            artista["nombre"] = normalizar_texto(
                artista["nombre"]
            )

        if "pais" in artista:

            artista["pais"] = normalizar_categoria(
                artista["pais"],
                "pais"
            )

        if "genero_musical" in artista:

            artista["genero_musical"] = normalizar_categoria(
                artista["genero_musical"],
                "genero_musical"
            )

        if "cache_eur" in artista:

            artista["cache_eur"] = limpiar_valor_numerico(
                artista["cache_eur"]
            )

    if len(lista_artistas) > 0:

        if "nombre" in lista_artistas[0]:

            lista_artistas = eliminar_duplicados(

                lista_artistas,

                ["nombre"]
            )

    return lista_artistas

# ============================================
# LIMPIAR CONCIERTOS
# ============================================

def limpiar_conciertos(
    lista_conciertos
):

    for concierto in lista_conciertos:

        if "fecha" in concierto:

            concierto["fecha"] = normalizar_fecha(
                concierto["fecha"]
            )

        if "escenario" in concierto:

            concierto["escenario"] = normalizar_categoria(
                concierto["escenario"],
                "escenario"
            )

    if len(lista_conciertos) > 0:

        if (

            "artista" in lista_conciertos[0]

            and

            "fecha" in lista_conciertos[0]
        ):

            lista_conciertos = eliminar_duplicados(

                lista_conciertos,

                ["artista", "fecha"]
            )

    return lista_conciertos

# ============================================
# LIMPIAR ENTRADAS
# ============================================

def limpiar_entradas(
    lista_entradas
):

    for entrada in lista_entradas:

        if "tipo_entrada" in entrada:

            entrada["tipo_entrada"] = normalizar_categoria(
                entrada["tipo_entrada"],
                "tipo_entrada"
            )

        if "precio" in entrada:

            entrada["precio"] = limpiar_valor_numerico(
                entrada["precio"]
            )

        if "fecha_compra" in entrada:

            entrada["fecha_compra"] = normalizar_fecha(
                entrada["fecha_compra"]
            )

        if "metodo_pago" in entrada:

            entrada["metodo_pago"] = normalizar_categoria(
                entrada["metodo_pago"],
                "metodo_pago"
            )

    if len(lista_entradas) > 0:

        if "id_entrada" in lista_entradas[0]:

            lista_entradas = eliminar_duplicados(

                lista_entradas,

                ["id_entrada"]
            )

    return lista_entradas

# ============================================
# LIMPIAR PATROCINADORES
# ============================================

def limpiar_patrocinadores(
    lista_patrocinadores
):

    for patrocinador in lista_patrocinadores:

        if "nombre" in patrocinador:

            patrocinador["nombre"] = normalizar_texto(
                patrocinador["nombre"]
            )

        if "categoria" in patrocinador:

            patrocinador["categoria"] = normalizar_categoria(
                patrocinador["categoria"],
                "categoria"
            )

        if "aportacion" in patrocinador:

            patrocinador["aportacion"] = limpiar_valor_numerico(
                patrocinador["aportacion"]
            )

    if len(lista_patrocinadores) > 0:

        if "nombre" in lista_patrocinadores[0]:

            lista_patrocinadores = eliminar_duplicados(

                lista_patrocinadores,

                ["nombre"]
            )

    return lista_patrocinadores

# ============================================
# CARGAR DATOS
# ============================================

artistas = cargar_csv(
    "./datos/artistas.csv"
)

conciertos = cargar_excel(
    "./datos/escenarios_horarios.xlsx"
)

patrocinadores = cargar_xml(
    "./datos/patrocinadores.xml"
)

entradas = cargar_json(
    "./datos/ventas_entradas.json"
)

# ============================================
# AUDITORÍA ANTES DE LIMPIAR
# ============================================

auditoria_artistas = auditar_datos(
    artistas,
    "artistas.csv"
)

auditoria_conciertos = auditar_datos(
    conciertos,
    "escenarios_horarios.xlsx"
)

auditoria_patrocinadores = auditar_datos(
    patrocinadores,
    "patrocinadores.xml"
)

auditoria_entradas = auditar_datos(
    entradas,
    "ventas_entradas.json"
)

# ============================================
# LIMPIEZA
# ============================================

artistas_limpios = limpiar_artistas(
    artistas
)

conciertos_limpios = limpiar_conciertos(
    conciertos
)

patrocinadores_limpios = limpiar_patrocinadores(
    patrocinadores
)

entradas_limpias = limpiar_entradas(
    entradas
)

# ============================================
# CREAR CARPETA DATOS_LIMPIOS
# ============================================

import os

os.makedirs(
    "./datos_limpios",
    exist_ok=True
)

# ============================================
# EXPORTAR CSV LIMPIOS
# ============================================

exportar_csv(

    artistas_limpios,

    "./datos_limpios/artistas_limpios.csv"
)

exportar_csv(

    conciertos_limpios,

    "./datos_limpios/conciertos_limpios.csv"
)

exportar_csv(

    patrocinadores_limpios,

    "./datos_limpios/patrocinadores_limpios.csv"
)

exportar_csv(

    entradas_limpias,

    "./datos_limpios/entradas_limpias.csv"
)

# ============================================
# EXPORTAR EXCEL GENERAL
# ============================================

datos_finales = {

    "Artistas": artistas_limpios,

    "Conciertos": conciertos_limpios,

    "Patrocinadores": patrocinadores_limpios,

    "Entradas": entradas_limpias
}

exportar_excel(

    datos_finales,

    "./datos_limpios/festival_limpio.xlsx"
)

# ============================================
# GUARDAR INFORME
# ============================================

auditorias = {

    "artistas.csv": auditoria_artistas,

    "escenarios_horarios.xlsx": auditoria_conciertos,

    "patrocinadores.xml": auditoria_patrocinadores,

    "ventas_entradas.json": auditoria_entradas
}

guardar_informe(
    auditorias
)

# ============================================
# FINAL
# ============================================

print(
    "\nPROCESO COMPLETADO"
)

print(
    "Datos limpios exportados correctamente"
)