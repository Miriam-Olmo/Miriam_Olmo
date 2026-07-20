nota = float(input('dime tu nota: '))

if nota >= 5 and nota <=10:
    print('estas aprobado🤩')
elif nota >= 0 and nota < 5:
    print('estas suspendido😒')
else:
    print('nota incorrecta❌')


if 0 <= nota < 5:
    print('Suspenso')
elif 5 <=  nota < 6:
    print('suficiente')
elif 6 <= nota < 7:
    print('bien')
elif 7 <=  nota < 9:
    print('notable')
elif 9 <= nota <= 10:
    print('sobresaliente')
else:
    print('revisar')