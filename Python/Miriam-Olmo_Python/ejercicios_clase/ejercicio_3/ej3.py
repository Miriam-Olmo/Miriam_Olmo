## Construir un programa que de por pantalla tres opciones
#      - 1 añadir un contacto a lista
#      - 2 leer todos los contactos de la lista
#      - 3 salir

# Si no pulso salir no me debe sacar de la aplicacion dandome opcion a elegir nuevamente cada vez que se termine mi eleccion anterior.

# lista_contactos sera un lista de diccionarios donde cada elemento tendrá los siguentes datos. Nombre, telefono, email

# Añadir un contacto deberá pedir esos datos y comprobar que nombre no es vacio, que telefono esta formado por digitos,y que el email estan bien escrito, al menos tiene que tener @. Si esto ocurre añadimos el contacto si no lanzamos un error y volvemos al menu principal 

# Leer contacto mostrara todos los contactos por pantalla

# opcion 1: importando todo el fichero funtions
#import lib.functions as fn
# opcion 2: importando solo las funciones que necesitamos
from lib.funtions import insertar_contacto, validar_contacto, pintar_contactos

agenda = []



def main():
    menu = """### Directorio de Contactos ####
[1]. Añadir contacto a lista
[2]. Leer todos los contactos
[3]. Salir
################################
"""
    print(menu)
    option = input('Dime que opción quieres: ')
    if option == '1':
       nombre = input('Introduce tu nombre: ')
       email = input('Introduce tu email: ')
       telefono = input('Introduce tu teléfono: ')
       es_valido = validar_contacto(nombre, email, telefono)
       if es_valido:
        insertar_contacto(nombre, email, telefono, agenda)
       else: 
          print(' los datos introducidos no son correctos, prueba de nuevo') 
    elif option == '2':
        pintar_contactos(agenda)
    elif option == '3':
        print('hasta pronto')
        return
    else:
        print('opcion no valida')
    main()

main()