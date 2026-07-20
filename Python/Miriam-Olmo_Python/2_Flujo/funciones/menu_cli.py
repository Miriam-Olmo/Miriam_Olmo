# vamos a crear un menu que me permita decidir que operacion va a hacer mi calculadora.

def pedir_numeros():
        numero1 = float(input('dime un numero: '))
        numero2 = float(input('dime un numero: '))
    

def main():
    menu = """
    ## BIENVENIDO A NUESTRA MARAVILLOSA CALCULADORA ##
    --------------------------------------------------
    [1] Sumar
    [2] Restar
    [3] Multiplicar
    [x] Salir   
    """
    print(menu)
    opcion = input('    ¿Que operación quieres realizar?: ')
    if opcion == '1':
        numeros = pedir_numeros()
        resultado = numeros[0] + numeros[1]
        print(resultado)
    elif opcion == '2':
        numeros = pedir_numeros
        resultado = numeros[0] - numeros[1]
        print(resultado)
    elif opcion == '3':
        numeros = pedir_numeros
        resultado = numeros[0] * numeros[1]
        print(resultado)
    elif opcion == 'x':
        print('vuelve pronto')
        return False
    else:
        print('opcion no valida, introduce de nuevo la opcion. ')
    main()
    
main()