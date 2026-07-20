def sumar(n1,n2,n3):
    return n1 + n2 + n3

def dividir(divisor, dividendo):
    return divisor / dividendo


def  media(n1, n2, n3):
    suma = sumar(n1, n2, n3)
    media = dividir(suma, 3)
    print(media)

n1 = float(input('dime un numero: '))
n2 = float(input('dime un numero: '))
n3 = float(input('dime un numero: '))


media(n1, n2, n3)


