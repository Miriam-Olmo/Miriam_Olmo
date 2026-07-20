# necesito una funcion que reciba el nombre del fichero, lo abra, lo lea y me devuelva la suma total de todos los productos del carrito

def sumar_carrito(carrito):
    try:
        mi_fichero = open(f"{carrito}.txt", 'r', encoding='UTF-8')
        # para leer el fichero linea a linea readlines()
        suma = 0
        for linea in mi_fichero.readlines():
            linea = linea.replace('\n', '')
            conjunto = linea.split(': ')
            suma += float(conjunto[1])
        else:
            mi_fichero.close() 
        print(suma)
    except FileNotFoundError:
        print('El fichero no existe')
    
    
# sumar_carrito('lista')
sumar_carrito('carrito')

