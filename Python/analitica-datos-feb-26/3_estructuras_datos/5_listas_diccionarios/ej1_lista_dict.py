# quiero un menu cli, 2 opciones insertar contacto y salir
# crear un lista de contactos vacia.
# contactos = []
# en la opcion 1 inserta contacto pedir los datos de contacto, nombre y telefono. E insertarlo en la lista.
# podremos insertar los contactos que queramos antes de salir
contactos = []

def limpiadora_datos(texto):
    # paso 1: pasar a minuscula
    texto = texto.lower()
    # paso 2: quitar acentos
    lista_vocales_acentos = ['á', 'é', 'í', 'ó', 'ú', 'ü']
    lista_vocales = ['a', 'e', 'i', 'o', 'u', 'u']
    for i in range(len(lista_vocales_acentos)):
        texto = texto.replace( lista_vocales_acentos[i], lista_vocales[i] )
    return texto

def insertar_contacto(nombre, tlf, lista):
    # paso 1: crear el diccionario
    contacto_nuevo = {
        'nombre': limpiadora_datos(nombre),
        'telefono': tlf
    }
    # paso 2: añadir el diccionario a la lista
    lista.append( contacto_nuevo )
    print('## Contacto añadido correctamente ##')

## opcion 2: pintar la lista contactos 
# Juan Antonio : 9876543
# ----------------------
# Miguel Angel: 567899
# ----------------------
def pintamos_agenda(lista):
    for contacto in lista:
        print( " " )
        print(contacto['nombre'])
        print('-------------------')
        print(contacto['telefono'])  
        print( " " )
        print('###')
        
def borrar_contacto(lista, nombre=""):
    if nombre != "":
        for contacto in lista:
            if contacto['nombre'] == nombre:
                # este es el contacto que quiero borrar
                lista.remove(contacto)
            
        print(f'### contacto con nombre {nombre} eliminado ###')
    else:
        #borramos el ultimo
        lista.pop()
        print('### Último contacto borrado correctamente ###')
  

def main():
    menu = """## Bienvenido a la agenda de contactos ##
[1]. Insertar un contacto
[2]. Listar contactos
[3]. Borrar el ultimo contacto de la agenda
[4]. Borrar un contacto por nombre
[x]. Salir de la app
"""
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        nombre = input('Dime el nombre del contacto: ')
        telefono = input('Teléfono: ')
        insertar_contacto(nombre, telefono, contactos)
    elif option == '2':
        pintamos_agenda(contactos)
    elif option == '3':
        # si no le paso nombre borro el último contacto
        borrar_contacto(contactos)
    elif option == '4':
        # borramos por nombre
        nombre = input('Dime el nombre a borrar: ')
        # limpiar los datos
        nombre = limpiadora_datos(nombre)
        borrar_contacto(contactos, nombre)
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    main()

main()