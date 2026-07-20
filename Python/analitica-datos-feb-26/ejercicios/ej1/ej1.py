numeros = [4, -2, 7, -5, 0, 3, -1, 8, 0, -9, 6]

# Crea una función clasificar_numeros(lista) que reciba una lista de números y devuelva tres listas: positivos, negativos y ceros.
def clasificar_numeros(lista):
    positivos = []
    negativos = []
    ceros = [] 
    for numero in lista:
        if not str(numero).isdigit() and str(numero)[0] != '-':
            continue
        elif numero > 0:
            positivos.append(numero)
        elif numero < 0:
            negativos.append(numero)
        elif numero == 0:
            ceros.append(numero)
        
    print(ceros)
    print(positivos)
    print(negativos)      
    


clasificar_numeros(numeros)


# Crea también una función estadisticas(lista) que devuelva la suma, el mayor numero, menor numero y la media

def estadisticas(lista):
    print( f"el número máximo es {max(lista)}" )
    print( f"el número mínimo es {min(lista)}" )
    print( f"la suma es igual {sum(lista)}" )
    print(f"la media es {sum(lista) / len(lista)}")


estadisticas(numeros)

