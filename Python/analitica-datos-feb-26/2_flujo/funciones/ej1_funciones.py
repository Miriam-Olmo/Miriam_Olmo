# quiero una funcion que me permita calcular sumas, restas y multiplicaciones de dos numeros.
# pablo sumar()
def sumar(numero_A, numero_B):
    return numero_A + numero_B

# reiner dividir()
def restar(numero_A, numero_B):
    return numero_A - numero_B

# miriam multiplicar
def multiplicar(n_A, n_B):
    return n_A * n_B
    
# juanan
def calcular(n1,n2, operacion):
    resultado = 0
    if operacion == 'sumar':
        resultado = sumar(n1, n2)
    elif operacion == 'restar':
        resultado = restar(n1, n2)
    elif operacion == 'multiplicar':
        resultado = multiplicar(n1, n2)
    else:
        print('operacion no valida')
    print(resultado)  
    
calcular(12,2,'fumar')