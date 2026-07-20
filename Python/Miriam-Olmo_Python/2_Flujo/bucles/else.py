# todos los bucles tienen una secuencia de escape que se lanza siempre que el bucle se completa


for i in range(1, 10):
    if i % 5 == 0:
        continue
    print(i)
else:
    print('el bucle ha terminado')



for i in range(1, 20):
    if i % 5 == 0:
        break
    print(i)
else:
    print('el bucle ha terminado')