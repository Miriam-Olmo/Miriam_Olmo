# Ejercicio: Gestor de Inventario de Tienda
# Objetivo: Crear un script que procese una lista de productos, calcule valores, aplique descuentos y muestre alertas de bajo stock.
# Instrucciones:
# Define una función llamada procesar_inventario(lista_productos).
# La función debe recibir una lista de tuplas, donde cada tupla es (nombre_producto, cantidad, precio_unitario).
# Dentro de la función, utiliza un bucle para recorrer los productos.
# Condicionales:
# Si la cantidad es menor a 5, imprimir: "Alerta: Producto [nombre] con bajo stock".
# Si el precio_unitario es mayor a 100, aplicar un 10% de descuento al precio.
# Si no, aplicar un 5% de descuento.
# Cálculos: Calcular el valor total del inventario de ese producto (cantidad * precio final con descuento).
# Salida: Imprimir el nombre del producto, el nuevo precio y el valor total.
# Al final, la función debe devolver el valor total de todo el inventario de la tienda. 
#conceptos necesarios

# Definición de funciones: def nombre():.
# Bucle For: for item in lista:.
# Estructuras condicionales: if, elif, else.
# Manipulación de datos: Operaciones aritméticas, tuplas

def revisar_inventario(lista_productos):
    valor_total_inventario = 0
    total_unidades = 0
    
    # Iteramos directamente sobre la lista de tuplas
    for nombre, cantidad, precio in lista_productos:
        # 1. Alerta de stock (usando f-string)
        if cantidad < 5:
            print(f"Alerta: {nombre} con bajo stock ({cantidad} unidades)")

        # 2. Lógica de descuento
        if precio > 100: 
            precio_con_descuento = precio * 0.9
        else:
            precio_con_descuento = precio * 0.95
        
        # 3. Cálculos por producto
        subtotal_producto = cantidad * precio_con_descuento
        
        # 4. Acumular totales globales
        valor_total_inventario += subtotal_producto
        total_unidades += cantidad
        
        # Opcional: imprimir info de cada producto procesado
        print(f"Procesado: {nombre} | Precio final: {precio_con_descuento:.2f} | Subtotal: {subtotal_producto:.2f}")

    return valor_total_inventario, total_unidades

# Datos de prueba
lista_productos = [
    ("Laptop", 3, 1200.00),
    ("Mouse", 10, 25.50),
    ("Monitor", 4, 150.00),
    ("Teclado", 20, 45.00),
    ("Cable HDMI", 2, 10.00)
]

# Llamada a la función
total_dinero, total_stock = revisar_inventario(lista_productos)

print("-" * 30)
print(f"Valor total del inventario (con descuentos): €{total_dinero:.2f}")
print(f"Total de productos en stock: {total_stock}")