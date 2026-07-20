import pandas as pd

# como cargar un fichero json
df_json = pd.read_json('./data/empleados.json')
# pintar el dataframe
print(df_json)
# por necesidad convertirlo de una lista
print(df_json.to_dict('records'))
print('-'*60)
# como casrgar un fichero xml
df_xml = pd.read_xml('./data/empleados.xml')
print(df_xml)
print('-'*60)
# como cargar un ficehro csv
df_csv = pd.read_csv('./data/empleados.csv')
print(df_csv)
print('-'*60)
# como cargar un fichero excel
df_excel = pd.read_excel('./data/empleados.xlsx', sheet_name='Empleados')
print(df_excel)
print('-'*60)
# como cargar un fichero txt
df_txt = pd.read_csv('./data/notas_python.txt')
print(df_txt)


