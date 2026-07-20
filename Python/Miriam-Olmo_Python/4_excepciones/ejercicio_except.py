"""
Tu objetivo es escribir un programa que haga lo siguiente:
Crea una lista con 5 recompensas (textos).
Pide al usuario que introduzca el número de la recompensa que quiere extraer (del 0 al 4).

Utiliza un bloque try-except-finally para controlar los posibles errores:

Maneja el ValueError: Si el usuario escribe letras en lugar de un número.

Maneja el IndexError: Si el usuario escribe un número que no está en la lista (por ejemplo, el 9 o el 25).

El programa debe imprimir siempre al final (haya fallado o no) un mensaje que diga: "Cerrando el catálogo de recompensas. ¡Gracias por jugar!".    
    
"""

def jugar():
    recompensas = ["Espada de madera", "Poción de salud", "Escudo", "Botas de velocidad", "Oro"]
    try:
        numero = int(input('dime que recompensa quieres: '))
        print(recompensas[numero])
    except IndexError:
        print('Dentro del listado no existe esta recompensa')
        jugar()
    except ValueError:
        print('la recompensa tiene que ser un numero')
        jugar()
    finally:
        print('cerrando el catalogo de recompensas. gracias por jugar')        
        
jugar()

