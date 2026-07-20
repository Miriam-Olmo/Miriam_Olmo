productos = [
    {
        'id': 1,
        'titulo': 'Leche desnatada',
        'precio': 0.56,
        'cantidad': 3
    },
    {
        'id': 2,
        'titulo': 'seitan',
        'precio': 3.45,
        'cantidad': 3
    }
]

# pintar todos los productos de la lista.

def pintar_productos(lista):
    for producto in lista:
        print('-------------------')
        print( producto['titulo'], producto['precio'], producto['cantidad'] )
    
#pintar_productos(productos)

# pedir por pantalla los datos de un producto, insertarlo en el listado de productos.

def insertar_producto(titulo, precio, cantidad):
    # titulo = input('Dime el producto que quieres insertar: ')
    # precio = float(input('Dime el precio del producto: '))
    # cantidad = int(input('Dime la cantidad de producto: '))
    contador = 3
    # paso 1: crear un diccionario con los datos pedidos por pantalla
    producto_nuevo = {
        'id': contador,
        'titulo': titulo,
        'precio': precio,
        'cantidad': cantidad
    }
    # paso 2: insertar ese diccionario en la lista general de productos
    productos.append(producto_nuevo)
    
   
    
insertar_producto('huevos', 2, 12)
insertar_producto('carne', 12, 2)
insertar_producto('calabacines', 1, 10)
# paso 3: pintar los productos
pintar_productos(productos)