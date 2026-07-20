"""
    Cálculo del precio a pagar en un aparcamiento
    - Pedir el número de horas que ha estado aparcado (número decimales permitidos)
        - El número de horas debe ser mayor de 0
    - Pedir si tiene tarjeta residente o no ("s" o "n")
        - La opción solo puede ser s o n
    - Pedir el tipo de vehículo ("moto", "coche", "furgoneta")
        - El tipo de vehículo debe ser moto, coche o furgoneta
    - Validamos los datos

    - Cálculo el precio dependiendo de las horas:
        - Primera hora: 2€
        - De 1 a 3 horas: 1.5€ por hora adicional
        - Más de 3 horas: 1€ por hora adicional a partir de la 3ª

    - Multiplicador de precio dependiendo del vehículo:
        moto x 0.7, coche x 1, furgoneta x 1.5

    - Aplica 20% descuento sobre el precio si erees residente

    FORMATO:
    --- TICKET DE APARCAMIENTO ---
    Horas: 2.5 | Vehículo: coche | Residente: sí
    Precio base: 3.75 €
    Descuento residente: -0.75 €
    TOTAL: 3.00 €
"""


# correccion

nº_horas = float(input('dime las horas de uso: '))
residente = input("¿tienes tarjeta residente [s/n]?"). lower()
vehiculo = input("tipo de vehiculo [coche/moto/furgoneta]"). lower()

if nº_horas <= 0:
    print('error!!!')
elif residente != "s" and residente != "n":
    print("solo acepta s o n")
# elif residente not in ("s", "n")
elif vehiculo not in ("moto", "coche", "furgoneta"):
    print("tipo no valido")
else:
    # hacemos el calculo

    if nº_horas <= 1:
        precio = 2
    elif nº_horas <= 3:
     precio = 2 + (nº_horas-1) *1.5
    else:
      precio = 2 + (2*1.5) + (nº_horas-3) 
    #primera hora (2€) + siguientes dos horas (1.5€) + resto de horas (1€)
    print( f'has estado {nº_horas} horas. precio a pagar {precio}€')

    # calculo multiplicar por vehiculo

    if vehiculo == "moto":
      multiplicador = 0.7
    else:
       multiplicador = 1.5

total = precio * multiplicador

#descuento residente

descuento = total * 0.2  if residente ==  's' else 0

total -= descuento

print(f"""
 --- TICKET DE APARCAMIENTO ---
    Horas: {nº_horas} | Vehículo: {vehiculo} | Residente: {residente}
    Precio base: {precio} €
    Descuento residente: -{round(descuento)} €
    TOTAL: {total} €
""")