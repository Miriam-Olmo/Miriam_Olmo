# crear un programa en python que me permita hacer una lista de la compra, 
# Un menu con tres opciones
   # [1]. Añadir un producto (nombre, cantidad)
   # [2]. Mostrar Lista de la compra
   # [3]. Borrar lista
   # [x]. Salir 
   
# trabajamos con modulos separados. modulo principal y secundario

# el fichero se llamará lista_compra.txt
from lib.functions import add_item, show_shoppingcart, delete_shoppingcart


def main():
    menu = """Bienvenido a lista Compra
[1]. Añadir un producto
[2]. Mostrar Lista de la compra
[3]. Borrar lista
[x]. Salir 
    """
    print(menu)
    option = input('Dime que opción quieres: ')
    if option == '1':
        nombre = input('Que producto necesitas: ').strip()
        cantidad = input('Cuantos necesitas: ').strip()
        msg = add_item(nombre, cantidad)
    elif option == '2':
        msg = show_shoppingcart()
    elif option == '3':
        msg = delete_shoppingcart()
    elif option == 'x':
        print('Hasta pronto')
        return 
    print(msg)
    main()


main()
