producto = {
    "title": "Televisión 4k 55 pulgadas",
    "price": 899,
    "quantity": 2,
    "tax": 21
}

producto1 = {
    "title" : 'Sillón de masaje',
    "price": 455,
    "quantity": 4,
    "tax": 10
}

# suponer que esto es un carrito de una compra de pagina web
# quiero calcular el PVP ( precio venta al publico ) del producto.

# PVP = (precio * cantidad) + (precio * cantidad) * 0.21 

def calcular_pvp(producto_dict):
    pvp = (producto_dict['price'] * producto_dict['quantity']) + ((producto_dict['price'] * producto_dict['quantity']) * producto_dict["tax"]/ 100)
    print(pvp)
    
calcular_pvp(producto)
calcular_pvp(producto1)