import csv

def carga_fichero(carpeta, nombre):
    fichero = open(f"./{carpeta}/{nombre}", "r", encoding="UTF-8")
    lector = csv.DictReader(fichero)
    lista = list(lector)
    fichero.close()
    return lista

# id,titulo,genero,precio,lanzamiento,en_stock
def pintar_bbdd(juegos, stock):
    for game in juegos:
        if int(game['en_stock']) == stock:
            print('=' * 50)
            print( f"{game['titulo']} - {game['genero']} => precio: {game['precio']} - {game['lanzamiento']}"  )
                      
def crear_fichero(carpeta, nombre, datos):
    fichero = open(f'./{carpeta}/{nombre}', 'w', encoding='UTF-8')
    cabeceras = []
    for key in datos[0].keys():
        cabeceras.append(key)
    mi_csv = csv.DictWriter(fichero, fieldnames=cabeceras)
    # escribir el documento fisico y guardarlo localmente
    mi_csv.writeheader()
    mi_csv.writerows(datos)
    fichero.close()
    
def aplicar_descuento(datos, descuento):
    for game in datos:
        valor_descuento = (float(game['precio']) * descuento) / 100
        resultado = float(game['precio']) - valor_descuento
        game['precio_descuento'] = str(round(resultado,2))
    return datos    
    
    
    
juegos = carga_fichero('data', 'game.csv')
#pintar_bbdd(juegos, 0)
#crear_fichero('data', 'juanan.csv', juegos)
juegos_20 = aplicar_descuento(juegos, 20)
crear_fichero('data', 'rebajas.csv', juegos_20)

# obtener el juego mas caro y mas barato
""" def valor_maximo(datos):
    maximo = 0
    juego_precio_maximo = {}
    for game in datos:
        if float(game['precio']) > maximo:
            maximo = float(game['precio'])
            juego_precio_maximo = game
    print(juego_precio_maximo)
            
valor_maximo(juegos)

def valor_minimo(datos):
    minimo = 1000
    juego_precio_minimo = {}
    for game in datos:
        if float(game['precio']) < minimo:
            minimo = float(game['precio'])
            juego_precio_minimo = game
    print(juego_precio_minimo)
            
valor_minimo(juegos)
"""

def calcular_precio_max_min(datos, tipo):
    valor_busqueda = float(datos[0]['precio'])
    juego_buscado = datos[0]
    for game in datos:
        if float(game['precio']) > valor_busqueda and tipo == 'max':
            valor_busqueda = float(game['precio'])
            juego_buscado = game
        elif float(game['precio']) < valor_busqueda and tipo == 'min':
            valor_busqueda = float(game['precio'])
            juego_buscado = game
    
    if tipo != "max" and tipo != "min":
        print('El tipo es incorrecto')
    else:     
        print(juego_buscado)


calcular_precio_max_min(juegos, 'max')

