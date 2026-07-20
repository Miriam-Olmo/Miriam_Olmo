# una funcion puede devolver uno o varios parametros para usarlos fuera de la funcion

def sumar(n1, n2):
    resultado = n1 + n2 # variable de ambito local
    return resultado

resultado = sumar(3, 4)
print(resultado)

sumar(3, 4)