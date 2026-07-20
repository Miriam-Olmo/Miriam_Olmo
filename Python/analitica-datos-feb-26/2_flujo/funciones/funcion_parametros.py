# una funcion puede tener dos tipos de parametros
        # obligatorios
        # optativos
numero_1 = 4
numero_2 = 23        

def sumar(numero_a, numero_b):
    resultado = numero_a + numero_b
    print(resultado)
    
sumar(23, 8)
sumar(numero_1, numero_2)


# funcion de potencia 3 elevado a 4 (10 elevado 6) y que valga para cualquier numero.
def potencia(base=4, exponente=3):
    resultado = base ** exponente
    print(resultado)

potencia()
potencia(10, 6)

# media de tres numeros cualesquiera
# pista la suma de los tres numeros divido entre la cantida

def media(numero_1, numero_2, numero_3):
    suma = numero_1 + numero_2 + numero_3
    media = suma / 3
    print(media)
    
media(2,3,5)






