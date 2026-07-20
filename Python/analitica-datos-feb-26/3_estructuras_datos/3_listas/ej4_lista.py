# =============================================================================
# EJERCICIO 4: NOTAS DE CLASE — INSERTAR, ORDENAR Y ESTADÍSTICAS
# Tienes una lista de notas de un examen.
# Añade tres notas más con append() y una en la posición 2 con insert().
# Muestra la lista ordenada de mayor a menor.
# Calcula y muestra la media, la nota más alta y la más baja.
# Cuenta cuántos alumnos han aprobado (nota >= 5).
# notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
# =============================================================================
notas = [7.5, 4.0, 8.5, 6.0, 9.0, 3.5, 5.5]
# menu, pintar el menu con las opciones - lista notas, añadir una nota al final, añadir una nota por posicion, mostrar la lista ordenada, calcular media, calcular maximo, calcular minimo, cuantos alumnos han aprobado. salir
def mostrar_notas(notas):
    for nota in notas:
        #print(nota)
        color = "1" if nota < 5 else "2"
        print( f'\033[3{color}m {nota} \033[0m' )
        
def inserta_nota(nota, posicion=len(notas)):
    notas.insert(posicion, nota)    

def sumar(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma

def calcular_media(notas):
    suma = sumar(notas)
    print(f'La media de las notas es: {round(suma/len(notas), 2)}')

# opcion 1: junior
def contar_notas(notas):
    contador = 0
    for nota in notas:
        if nota >= 5:
            contador += 1
    return contador

# opcion 2: senior
def contar_notas_senior(notas, tipo='aprobados'):
    lista_aprobados = list(filter(lambda nota: nota >= 5, notas))
    if tipo == 'suspensos':
        return len(notas) - len(lista_aprobados)
    return len(lista_aprobados)

def main():
    menu = """## Bienvenido a la aplicación de notas ##
    [1]. Listar la notas
    [2]. Añadir nueva nota
    [3]. Añadir nueva nota en cualquier posición
    [4]. Ordenar de mayor a menor
    [5]. Calcular media
    [6]. Calcular máximo
    [7]. Calcular mínimo
    [8]. Numero de alumnos aprobados
    [x]. Salir
    """
    print(menu)
    option = input('Dime que opcion quieres: ')
    print('-' * 40)
    if option == '1':
        mostrar_notas(notas)
    elif option == '2':
        nota = float(input('Dime una nota: '))
        inserta_nota(nota)
    elif option == '3':
        nota = float(input('Dime una nota: '))
        posicion = int(input('Dime en que posicion: '))
        inserta_nota(nota, posicion)
    elif option == '4':
        notas_ordenadas = sorted(notas,reverse=True)
        mostrar_notas(notas_ordenadas)
    elif option == '5':
        calcular_media(notas)
    elif option == '6':
        print(f'El nota máxima es {max(notas)}')
    elif option == '7':
         print(f'El nota mínima es {min(notas)}')
    elif option == '8':
        tipo = input('¿Qué buscas, aprobados o suspensos?: ')
        numero = contar_notas_senior(notas, tipo)
        print(f"el numero de {tipo} es igual a {numero}")
    elif option == 'x':
        print('Hasta pronto')
        return
    else:
        print('Opcion no valida')
    print('-' * 40)
    print(' ')
    main()
    


main()
