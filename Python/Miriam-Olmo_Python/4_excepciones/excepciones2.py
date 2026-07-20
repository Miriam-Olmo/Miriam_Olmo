
try:
    numero1 = int(input('dime un numero: '))
    numero2 = int(input('dime otro numero: '))
    resultado = numero1 / numero2
    print(resultado)

except ValueError:
    print('los valores introducidos no son numeros')
except ZeroDivisionError:
    print('no se puede dividir por cero')
except:
    print('futuro error no previsto')


