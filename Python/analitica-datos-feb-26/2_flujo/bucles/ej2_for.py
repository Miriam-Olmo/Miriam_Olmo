# pintar por pantalla 1000 numeros pero solo los pares. Empezando de 1 hasta 1000. No se puede cambiar los valores iniciales.

# paso 1: bucle desde 1 hasta 1000
# paso 2: pintar 1000 numeros
# paso 3: pintar solo los pares. Tiene que funcionar para impares tambien.

for i in range(1, 1000):
    if i % 2 != 0:
        print(i)

