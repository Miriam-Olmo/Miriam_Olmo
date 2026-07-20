nota = float(input('Dime tu nota: '))

if nota >= 0 and nota < 5:
    print('Suspenso')
    print('Otra cosa')

if nota >= 5 and nota <= 10:
    print('Estás aprobado')

"""
    Pide por input el importe de una compra
    Si el importe es mayor que 100 muestra el mensaje:
        "Aplicamos un 10% de descuento"
        Y además, mostramos el precio con el descuento aplicado
"""
precio = float(input('Dime el importe: '))

if precio > 100:
    print('Aplicamos el 10% de descuento')
    precio_con_descuento = precio * 0.9
    print(f"Precio original: {precio}€. Precio Descuento: {precio_con_descuento}€")