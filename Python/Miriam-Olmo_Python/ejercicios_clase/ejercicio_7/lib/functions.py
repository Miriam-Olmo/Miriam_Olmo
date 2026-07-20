def añadir_producto(nombre, cantidad):
    try:
        if nombre != "" and cantidad != "" and int(cantidad) > 0 :
            fichero = open('./data/lista_compra.txt', 'a', encoding='UTF-8')
            fichero.write(f'{nombre} => cantidad: {cantidad}\n')
            fichero.close()
            return 'Producto añadido correctamente'
        else:
            return 'No se pueden introducir valor vacios'
    except ValueError:
        return 'el valor introducido en cantidad tiene que ser un numero'

def ver_lista():
    print("--- COSAS POR COMPRAR ---")
    # Usamos try/except por si el archivo no existe todavía (así no da error)
    fichero = open(f'./data/lista_compra.txt', "r", encoding='UTF-8')
    lineas = fichero.readlines()
    if len(lineas) == 0:
        return 'no hay productos en el carrito'
    for linea in lineas:
        print('-'*20)
        linea = linea.replace('\n', '')
        linea = linea.replace(' =>', ':\n ')
        print(linea)
    else:
        print('-'*20)
    fichero.close()

def borrar_lista():
    fichero = open('./data/lista_compra.txt', 'w', encoding='UTF-8')
    fichero.close()
    return 'lista compra vacia'
