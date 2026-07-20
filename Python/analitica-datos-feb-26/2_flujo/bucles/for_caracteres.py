texto = "Pablo Pérez"

# un string es un cadena de caracteres, es decir es un conjunto de caracteres.

# cuantos caracteres tiene un texto.
print( len(texto) ) # cantidad de caracteres
print(texto[0]) # J
print(texto[5]) # A

for i in range(len(texto)):
    print(texto[i])
    
# upper() lower()
# imprimais solo las mayusculas

for i in range(len(texto)):
    if texto[i] == texto[i].upper():
        print(texto[i])



