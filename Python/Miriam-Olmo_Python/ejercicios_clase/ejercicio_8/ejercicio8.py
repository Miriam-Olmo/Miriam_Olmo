import csv

def cargar_fichero(carpeta, nombre):
    fichero = open(f"./{carpeta}/{nombre}", "r", encoding="UTF-8")
    lector = csv.DictReader(fichero)
    lista = list(lector)
    fichero.close()
    return (lista)


def pintar_bbdd(juegos, stock):
    for game in juegos:
        if int(game['en_stock']) == stock:
            print('='*20)
            print(f'{game['titulo']} - {game['genero']} => precio: {game['precio']} - {game['lanzamiento']}')


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
        valor_descuento = (float(game['precio'])*descuento)
        resultado = float(game['precio']) - valor_descuento
        game['precio_rebajado'] = str(round(resultado,2))
        return datos


"""# obtener el juego más caro y más baratos
def valor_max(datos):
    maximo = 0
    juego_precio_max = {}
    for game in datos:
        if float(game['precio']) > maximo:
            maximo = float(game['precio'])
            juego_precio_max = game
    print(juego_precio_max)


def valor_minimo(datos):
    minimo = 1000
    juego_precio_minimo = {}
    for game in datos:
        if float(game['precio']) < minimo:
            minimo = float(game['precio'])
            juego_precio_minimo = game
    print(juego_precio_minimo)"""
            
def calcular_precio_max_min(datos, tipo):
    valor_busqueda = float(datos[0]['precio'])
    juego_buscado = datos[0]
    for game in datos:
        if float(game['precio']) > valor_busqueda and tipo == 'max':
            juego_buscado = game
        elif float(game['precio']) < valor_busqueda and tipo == 'min':
            juego_buscado = game
    if tipo != 'max' and tipo != 'min':
        print('el tipo es incorrecto')
    else:
        print(juego_buscado)


juegos = cargar_fichero('data', 'game.csv')
pintar_bbdd(juegos, 1)
juegos_20 = aplicar_descuento(juegos, 0.20)
crear_fichero('data', 'rebajas.csv', juegos_20)
# valor_max(juegos)
# valor_minimo(juegos)
calcular_precio_max_min(juegos, 'max')

