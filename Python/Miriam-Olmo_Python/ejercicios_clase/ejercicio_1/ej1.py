
numeros = [4, -2, 0, 7, -5, 0, 3, -1, 8, 0, -9, 6]

positivos = []

negativos = []

ceros = []



def clasificar_numeros(lista):
    for numero in lista:
        if not str(numero).isdigit() and str(numero)[0] != '-':
            continue
        elif numero > 0:
            positivos.append(numero)
            print('positivo')
        elif numero == 0:
            ceros.append(numero)
            print('ceros')
        elif numero < 0:
            negativos.append(numero)
            print('negativo')
        else:
            print('numero no valido')


    print(ceros)
    print(positivos)
    print(negativos)




clasificar_numeros(numeros)

def estadisticas(lista):
    print(f'el numero maximo es : {max(lista)}')
    print(f' el numero minimo es {min(lista)}')
    print(f'la suma es igual {sum(lista)}')
    print(f'la moda es {sum(lista) / len(lista)}')



estadisticas(numeros)