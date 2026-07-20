# se salta ese paso pero vuelve a entrar en el bucle

for i in range(1, 19):
    if i % 8 == 0:
        continue
    print(i)