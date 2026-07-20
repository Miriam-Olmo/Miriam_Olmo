# Modificar el ejercicio anterior para que admita numeros negativos

lista_numeros = []

while True:
    numero = input('Dime un numero: ')
    numero_sin_signo = numero.replace("-", "")
    if not numero_sin_signo.isdigit():
        break
    lista_numeros.append(int(numero))
    
print(lista_numeros)