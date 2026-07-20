# tenemos un producto

producto = ('Laptop Pro', 899.94, 15, "electronica")
producto2 = ('Raton gaming', 34.90, 100, "electronica")

# el primer elemento reprensenta el nombre producto
# el segundo el precio
# el tercero el stock
# categoria

# quiero que contruyais una funcion que me permita calcular el precio total del stock de este producto.

def calcular_precio_stock(producto):
    return producto[1] * producto[2]


precio_p1 = calcular_precio_stock(producto)
precio_p2 = calcular_precio_stock(producto2)

print(precio_p1, precio_p2)