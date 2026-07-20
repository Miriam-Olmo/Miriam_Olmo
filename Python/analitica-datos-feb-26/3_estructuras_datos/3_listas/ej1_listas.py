# pedir numeros por pantalla, insertarlos en una lista de numeros, el programa para cuando introduzcamos un letra y dicha letra no estará en la lista.

lista_numeros = []

while True:
    numero = input('Dime un numero: ')
    if not numero.isdigit():
        break
    lista_numeros.append(int(numero))
    
print(lista_numeros)
