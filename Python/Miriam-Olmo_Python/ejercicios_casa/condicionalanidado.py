# Ejercicio Condicional Anidado

nota = float(input('mete tu nota (0-10): '))

# Condicional externo: verifica la nota

if nota < 5:
    print('suspenso')
elif 5 <= nota < 6:
    print('bien')
elif 6 <= nota < 7:
    print('muy bien')
elif 7 <= nota < 8:
    print('notable')
elif 9 <= nota <= 10:
    print('sobresaliente')
else:
    print('revisar nota')