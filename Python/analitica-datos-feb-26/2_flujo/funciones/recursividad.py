# funcion recursiva es una funcion que se llama si misma

# def saludar():
#     print('hola')
#     saludar()
    
# saludar()

# crear una funcion que pida un dni solo los numeros y validar que es una cadena numerica. 

# proceso de validacion

def validar_dni():
    dni = input('Dime el numero de tu DNI: ')
    if dni.isdigit():
        print('Es un dni valido')
        return dni
    else:
        print('Esto no es un numero')
        validar_dni()
        
mi_dni = validar_dni()