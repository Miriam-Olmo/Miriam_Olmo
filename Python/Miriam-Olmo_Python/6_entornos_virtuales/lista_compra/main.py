# nos traemos cada una de la funciones que me permitan conectarme con los datos
from controllers.consultas_controller import get_compra, pintar_compra, eliminar_articulo, insertar_articulo, obtener_productos_prioridad

def init():
    menu = """##### Lista de compra #####
    [1]. Añadir articulo
    [2]. Eliminar articulo
    [3]. Ver la lista de la compra
    [4]. Obtener productos por prioridad
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opción eliges: ')
    if option == '1':
        try:
            nombre = input('Introduce el nombre del producto: ')
            precio = float(input('Introduce el precio del producto: '))
            cantidad = int(input('Introduce la cantidad del producto: '))
            prioridad = input('Introduce la prioridad, alta, media, baja: ').lower()
            if prioridad != 'alta' and prioridad != 'media' and prioridad != 'baja':
                raise Exception('La prioridad solo puede ser alta, media o baja')
            # creamos una tupla con todos valores para insertarlos en BBDD
            registro = (nombre, precio, cantidad, prioridad)
            result = insertar_articulo(registro)
            print(result)
        except ValueError:
            print('Precio y cantidad tienen que ser numeros')
        except Exception as e:
            print(f"Error: {e}")
           
        
    elif option == '2':
        id = input('Dame el id del articulo a eliminar: ')
        result = eliminar_articulo(int(id))
        print(result)
    elif option == '3':
       result = get_compra()
       pintar_compra(result)
    elif option == '4':
        try:
            prioridad = input('Dime la prioridad que quieres buscar, alta, media, baja: ')
            if prioridad != 'alta' and prioridad != 'baja' and prioridad != 'media':
                raise Exception('La prioridad solo puede ser alta, media o baja')
            
            result = obtener_productos_prioridad(prioridad)
            if result and len(result) != 0:
                pintar_compra(result)
            else:
                print('No hay resultados en esta busqueda')
        except Exception as e:
             print(f"Error: {e}")
    elif option.lower() == 'x':
        print('Hasta pronto')
        return False
    else:
        print('No es una opcion valida')
    init()



if __name__ == "__main__":
    init()