## vamos a crear un menu, que me permita decidir que operacion va hacer mi calculadora. 

def pedir_numeros():
    numero1 = float(input('Dime un numero: '))
    numero2 = float(input('Dime un numero: '))
    return numero1, numero2

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
    option = input('¿Que operación quieres realizar? ')
    resultado = 0
    if option == '1':
        numeros = pedir_numeros()
        resultado = numeros[0] + numeros[1]
    elif option == '2':
        numeros = pedir_numeros()
        resultado = numeros[0] - numeros[1]
    elif option == '3':
        numeros = pedir_numeros()
        resultado = numeros[0] * numeros[1]
    elif option == 'x':
        print('Hasta pronto, vuelve cuando quieras')
        return False
    else:
        print('valor introducido no valido, introduce de nuevo el valor')
    print(resultado)
    main()
    
main()