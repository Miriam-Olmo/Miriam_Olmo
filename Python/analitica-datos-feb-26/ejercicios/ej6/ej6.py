# Crea un script en Python que pida al usuario su número de ticket de compra y, tras validar que la entrada no contenga letras (mostrando un error si las hay) calcule el premio correspondiente

# ["Un Café Gratis", "10% de Descuento" , "Un Bolígrafo"]

# premio se obtiene resto el numero ticket entre 5. El dato obtenido es la posicion de la lista

# si el numero se sale rango no hay premio
def comprobar_premio():
    premios = ["Un Café Gratis", "10% de Descuento" , "Un Bolígrafo"]
    try:
        numero_ticket = int(input('Dime el numero de ticket: '))
        i = numero_ticket % 5
        print(f"{premios[i]}")
    except ValueError:
        print("El ticket solo puede tener numeros ")
    except IndexError:
        print("No tienes premio, el ticket se ha salido de rango ")
        
comprobar_premio()
        



















