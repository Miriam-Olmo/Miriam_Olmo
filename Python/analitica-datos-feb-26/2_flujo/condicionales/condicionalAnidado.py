nota = float(input("Dime tu nota: "))

if nota >= 5 and nota <= 10:
    print('Estás aprobado 🥳')
elif nota >= 0 and nota < 5:
    print('Estás suspenso 😢')
else: 
    print('La nota no es correcta')

if 0 <= nota < 5:
    print('suspenso')
elif 5 <= nota < 6:
    print('suficiente')
elif 6 <= nota < 7:
    print('bien')
elif 7 <= nota < 9:
    print('notable')
elif 9 <= nota <= 10:
    print('Sobresaliente')
else:
    print('Nota no válida')