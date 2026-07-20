# crear un programa en python que me permita hacer una lista de la compra, 
# Un menu con tres opciones
   # [1].Añadir un producto (nombre, cantidad)
   # [2].Mostrar Lista de la compra
   # [3]. Borrar lista
   # [x]. Salir 
   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt
from lib.functions import añadir_producto, ver_lista, borrar_lista

def main():
    menu = """
[1] añadir producto
[2] mostrar lista compra
[3] borrar lista
[x] salir
"""
    print(menu)

    opcion = input('que opcion quieres: ')
    if opcion == '1':
        nombre = input( 'que producto necesitas: ').strip()
        cantidad = input('cuantos quieres: ').strip()
        mensaje = añadir_producto(nombre.lower(), cantidad)
    elif opcion == '2':
        mensaje = ver_lista()
    elif opcion == '3':
        mensaje = borrar_lista()
    elif opcion == 'x':
        print('vuelve pronto')
        return
    print(mensaje)
    main()

main()

