
# nos traemos cada una de la funciones que me permitan conectarme con los datos
from controllers.consultas_controllers import get_compra,pintar_compra, eliminar_articulo

def init():
    menu = """ ### Lista de compra ###
    [1] añadir articulo
    [2] eliminar articulo
    [3] ver la lista
    [x] salir
    """
    print(menu)
    opcion = input('dime que opcion eliges: ')
    if opcion == '1':
        try:
            nombre = input('introduce el nombre del producto: ')
            precio = float(input('introduce el precio del articulo: '))
            cantidad = int(input('introduce la cantidad del articulo: '))
            prioridad = (input('introduce la prioridad, alta, media, baja: ')).lower()
            if prioridad != 'alta' and prioridad != 'media' and prioridad != 'baja':
                print('la prioridad solo puede ser alta, media o baja')
        except ValueError:
            print('precio y cantidad tienen que ser numeros')
    elif opcion == '2':
        id =input('dame el id del articulo: ')
        result = eliminar_articulo(int(id))
        print(result)
    elif opcion == '3':
        result = pintar_compra(get_compra())
        print(result)
    elif opcion.lower() == 'x':
        print('hasta pronto')
        return False
    else: 
        print('no es una opcion valida') 
    init()



if __name__ == "__main__":
    init()