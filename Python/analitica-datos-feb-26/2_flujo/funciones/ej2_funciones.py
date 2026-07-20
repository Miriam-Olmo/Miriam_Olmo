
def sumar(n1,n2,n3):
    return n1 + n2 + n3

def dividir(divisor, dividendo):
    return divisor / dividendo

def media(numero_1, numero_2, numero_3):
    suma = sumar(numero_1, numero_2, numero_3)
    media = dividir(suma, 3)
    print(media)
    
    
numero_1 = float(input('Dame un primer numero: '))
numero_2 = float(input('Dame un segundo numero: '))
numero_3 = float(input('Dame un tercer numero: '))
media(numero_1,numero_2,numero_3)