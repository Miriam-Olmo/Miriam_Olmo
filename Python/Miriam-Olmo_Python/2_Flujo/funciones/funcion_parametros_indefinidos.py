# *numeros representa un conjuto de datos, ese conjunto tiene posicion empezando en 0 y acaban n-1 siendo n la longitud o cantidad
def sumar(*numeros):
    resultado = 0
    for i in range(len(numeros)):
        resultado += numeros[i]
    print(resultado)
    print('--------')



sumar(1,2)
sumar(1,2,3)
sumar(1,2,3,4,5,12)


#media (1,2,3,4,5), media(2,3,4)



def media(*numeros):
    # primero obtener la suma de todos los numeros
    suma = 0
    for numero in numeros:
        suma += numero
    print(suma / len(numeros))



media(1,2,3,4,5)

media(2,3,4)