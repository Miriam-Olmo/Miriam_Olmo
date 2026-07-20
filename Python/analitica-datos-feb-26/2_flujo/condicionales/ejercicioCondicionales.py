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

horas = float(input("Dime cuántas horas has permanecido en el parking: "))
residente = input("¿Tienes tarjeta de residente [s/n]?: ").lower()
vehiculo = input("Tipo de vehículo [coche/moto/furgoneta]: ").lower()

if horas <= 0:
    print('Las horas deben ser un valor positivo')
# elif residente != "s" and residente != "n":
elif residente not in ('s', 'n'): 
    print('Responde s o n para la tarjeta de residente')
elif vehiculo not in ('moto', 'coche', 'furgoneta'):
    print('Tipo de vehículo no válido')
else:
    # Todo correcto - Hacemos el cálculo
    if horas <= 1:
        precio = 2
    elif horas <= 3:
        precio = 2 + (horas - 1) * 1.5
    else:
        # Primera hora (2€) + Siguientes dos horas (1.5€) + Resto de horas (1€)
        precio = 2 + (2 * 1.5) + (horas - 3)

    # Cálculo multiplicador x vehículo
    multiplicador = 1

    if vehiculo == 'moto':
        multiplicador = 0.7
    elif vehiculo == 'furgoneta':
        multiplicador = 1.5

    total = precio * multiplicador

    # Descuento residente
    descuento = total * 0.20 if residente == 's' else 0
    total -= descuento

    print(f"""
    --- TICKET DE APARCAMIENTO ---
    Horas: {horas} | Vehículo: {vehiculo} | Residente: {residente}
    Precio base: {round(precio)} €
    Descuento residente: -{round(descuento)} €
    TOTAL: {round(total)} €
    """)