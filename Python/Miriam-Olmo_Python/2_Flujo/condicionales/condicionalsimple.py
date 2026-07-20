nota = float(input('dime tu nota: '))

if nota >= 0 and nota < 5: 
    print("Suspenso")

if nota >= 5 and nota <= 10:
    print("Aprobadooooo!!!!")


    """
      Pide por input el importe de una compra
    Si el importe es mayor que 100 muestra el mensaje:
        "Aplicamos un 10% de descuento"
    Y además, mostramos el precio con el descuento aplicado
    """

    precio = float(input('dime el importe de la compra: '))

    if precio > 100:
        print('Aplicamos un 10% de descuento')
        precio_descuento = precio * 0.9
        print(f'precio original: {precio}€. precio descuento: {precio_descuento}€.')