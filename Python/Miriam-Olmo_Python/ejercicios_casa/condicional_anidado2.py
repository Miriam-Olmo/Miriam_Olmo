# Ejercicio 1: Clasificación de Edad y Permiso
# Este programa verifica si una persona es mayor de edad y, de ser así, si tiene permiso firmado. 

edad = int(input('dime tu edad: '))

if edad >= 18:
    print('eres mayor de edad')
    permiso = input('¿tienes permiso firmado? ')
    if permiso == 'si':
        print('puedes venir')
    else:
        print('necesita permiso firmado')
else:
    print('eres menor de edad, no puedes venir')


# Ejercicio 2: Sistema de Notas con Matrícula de Honor
# Este programa evalúa una nota numérica y anida condiciones para determinar si el estudiante tiene una calificación sobresaliente o matrícula de honor.

nota = float(input('introduce tu nota: '))

if 0 <= nota < 5:
    print('suspenso')
elif 5 <= nota < 9:
    print('aprobado')
elif 9 <= nota < 10:
    print('sobresaliente')
elif nota == 10:
    print('matricula de honor')
else:
    print('revisar nota')