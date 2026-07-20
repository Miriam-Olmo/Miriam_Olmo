def pedir_datos(option):
    try:
        if option == '1' or option == '2' or option == "3" or option == '4' or option == '5' or option == '6':
                n1 = float(input('Dime un numero: '))
                n2 = float(input('Dime otro numero: '))
                return n1, n2
        elif option == '7':
                base = float(input('Dame la base: '))
                exponente = int(input('Dame el exponente: '))
                return base, exponente
        elif option == '8':
                radicando = float(input('Dame el radicando de la raiz cuadrada: '))
                return radicando
    except ValueError:
        print('El valor introducido no es un numero')
        return False

def dividir(datos, option = '4'):
    try:
        # option 1: forma no abreviada
        # if option == '5':
        #     resultado = datos[0] // datos[1]
        # else:
        #     resultado = datos[0] / datos[1]
        # return resultado
        
        # option 2: forma abreviada
        return datos[0] // datos[1] if option == '5' else datos[0] / datos[1]
    except ZeroDivisionError:
        return 'No se puede dividir por cero'
    

def modulo(datos):
    try:
        return datos[0] % datos[1]
    except ZeroDivisionError:
        return 'El módulo no puede usar cero en el divisor'
    
    
def potencia(datos):
    try:
        return datos[0] ** datos[1]
    except OverflowError:
        return 'El exponente es demasiado grande'