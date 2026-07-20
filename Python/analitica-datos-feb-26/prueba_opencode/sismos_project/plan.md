# Plan de Trabajo: Proyecto EDA Sismos

## 1. Configuración del Entorno y Dependencias
- Crear un entorno virtual con Python 3.12 en la carpeta de trabajo:
  ```
  python3.12 -m venv .venv
  ```
- Generar `requirements.txt` con las siguientes dependencias:
  - pandas
  - numpy
  - seaborn
  - pymongo
  - jupyter
- Crear un archivo `.env` para la conexión a MongoDB:
  - Incluir al menos la variable `MONGO_URL` (ejemplo: `mongodb://localhost:27017/`).

## 2. Conexión y Extracción de Datos desde MongoDB
- Conectar a la base de datos local MongoDB (`sismosdb`) y la colección `sismos` desde Python, usando variables del `.env`.
- Crear función para la conexión segura siguiendo estándar (variables en inglés, snake_case, docstring breve terminando en "generado por ia").
- Extraer y cargar datos a un DataFrame (pandas).

## 3. Transformación y Limpieza de Datos
- Convertir los datos MongoDB a DataFrame.
- Limpiar duplicados, nulos y valores incongruentes:
  - Revisar campos obligatorios: magnitud, lugar, profundidad, etc.
  - Validar existencia y correcto formateo de latitud/longitud en `ubicacion`.

## 4. Análisis y Visualización
- Visualización de propuestas (todas con seaborn, pandas y/o matplotlib):
  1. **Top sismos por magnitud**: Barplot horizontal (top 10-20 por magnitud), mostrando lugar y fecha para identificar rápidamente los eventos extremos.
  2. **Frecuencia de sismos por ciudad/país en el tiempo**: 
      - Barplot para ranking total por ciudad/país.
      - Lineplot (serie temporal agregada por año/mes) para ver evolución temporal por los lugares más afectados.
  3. **Mapa coroplético**: Scatterplot geográfico (latitud/longitud) sobre un plano terrestre, coloreando los puntos por magnitud y/o frecuencia. Si seaborn no basta para el fondo, usar matplotlib base map para trazado de mapas simple, siempre evitando Plotly.

## 5. Documentación y Resultados
- Notebook `.ipynb`:
  - Uso de Markdown breve y conciso.
  - Inclusión de conclusiones y comentarios para cada gráfico.
  - Cumplimiento de reglas: inglés, snake_case en variables y funciones, docstrings, cierre con "generado por ia".

## 6. Verificación Final
- Probar el notebook en ambiente limpio (.venv activado).
- Validar que se conecta, procesa y visualiza correctamente.


