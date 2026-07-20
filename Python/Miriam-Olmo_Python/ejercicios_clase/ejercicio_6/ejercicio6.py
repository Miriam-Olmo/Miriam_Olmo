# Crea un script en Python que pida al usuario su número de ticket de compra y, tras validar que la entrada no contenga letras (mostrando un error si las hay) calcule el premio correspondiente

# ["Un Café Gratis", "10% de Descuento" , "Un Bolígrafo"]

# premio se obtiene resto el numero ticket entre 5. El dato obtenido es la posicion de la lista

# si el numero se sale rango no hay premio
def comprobar_premio():
    premios = ["Un Café Gratis", "10% de Descuento" , "Un Bolígrafo"]
    try:
        numero_ticket = int(input('Dime el numero de ticket: '))
        i = numero_ticket % 5
        print(f"\033[32m{premios[i]}\033[0m")
    except ValueError:
        print("\033[31m el ticket solo puede tener numeros \033[0m")
    except IndexError:
        print("\033[31m No tienes premio, el ticket se ha salido de rango \033[0m")
        
comprobar_premio()
    
    