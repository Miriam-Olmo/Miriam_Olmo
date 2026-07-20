# =============================================================================
# EJERCICIO 1: CALCULADORA CIENTÍFICA ROBUSTA
# Implementa una calculadora que soporte las operaciones:
#   +, -, *, /, // (división entera), % (módulo), ** (potencia), sqrt (raíz cuadrada)
#
# Requisitos de manejo de excepciones:
# - ValueError: si el usuario introduce algo que no es un número
# - ZeroDivisionError: para /, // y %
# - ValueError personalizado: si se pide sqrt de un número negativo
# - ArithmeticError: para desbordamientos en potencias extremas
# - OverflowError: captura específica
# - Excepción genérica como último recurso
# - Bloque finally: siempre muestra "Operación procesada"
# - El programa pide una nueva operación al terminar (recursivo o bucle)
# =============================================================================
import math
import lib.functions as fn

def main():
    try:
        menu = """# Calculadora cientifica #
    [1].sumar
    [2].restar
    [3].multiplicar
    [4].dividir
    [5].division entera
    [6].modulo
    [7].potencia
    [8].raiz cuadrada
    [x].Salida    
        """
        print(menu)
        option = input('Dime que quieres calcular: ')
        if option == '1':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = sum(datos)
                print(resultado)
        elif option == '2':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = datos[0] - datos[1]
                print(resultado)
        elif option == '3':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = datos[0] * datos[1]
                print(resultado)
        elif option == '4' or option == '5':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = fn.dividir(datos, option)
                print(resultado)
        elif option == '6':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = fn.modulo(datos)
                print(resultado)
        elif option == '7':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = fn.potencia(datos)
                print(resultado)
        elif option == '8':
            datos = fn.pedir_datos(option)
            if datos:
                resultado = math.sqrt(datos)
                print(resultado)
        elif option == 'x':
            print('Hasta pronto')
            return
        else:
            print('opcion no valida') 
    except:
        print('error generico')
    finally:
        print('Operación procesada')
    main()
    
main()