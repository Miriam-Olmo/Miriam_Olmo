"""
El cálculo de la letra del Documento Nacional de Identidad (DNI) es un proceso matemático sencillo que se basa en obtener el resto de la división entera del número de DNI y el número 23. 
A partir del resto de la división, se obtiene la letra seleccionándola dentro de un lista de letras.

El array de letras es:
letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B','N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E','T'];

Por tanto si el resto de la división es 0, la letra del DNI es la T y si el resto es 3 la letra es la A. 
Con estos datos, elaborar un pequeño script que:

1. Almacene en una variable el número de DNI indicado por el usuario y en otra variable la letra del
DNI que se ha indicado.

2. Si el numero no introducido no esta formado por numeros solo deberá para la ejecución y lanzar 
un error de numero no valido.

3. Si el número es válido, se calcula la letra que le corresponde según el método explicado
anteriormente.

4. Una vez calculada la letra, se debe comparar con la letra indicada por el usuario. Si no coinciden, 
se muestra un mensaje al usuario diciéndole que la letra que ha indicado no es correcta. En otro caso, se muestra un mensaje indicando que el número y la letra de DNI son correctos.     
"""

def main():
    dni = input('dime tu dni: ').upper()
    dni = dni.zfill(9)
    print(dni)
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B','N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'] 
    # paso 1: comprobar si el dni tiene 9 o menos caracteres
    if len(dni) > 9:
        print('Dni no valido')
        return 
    # paso 2: extraer la letra y el numero del dni
    letra = dni[-1]
    numero = int(dni[:-1]) # numero sin la letra
    i = numero % 23
    letra_correcta = letras[i]
    
    # if letra != letra_correcta:
    #     print(f'Dni {dni} no valido')
    # else:
    #     print(f'Dni {dni} valido')
    
    # condicional abreviado
    resultado = 'no' if letra != letra_correcta else ""
    print(f'Dni {dni} {resultado} valido')
    

main()