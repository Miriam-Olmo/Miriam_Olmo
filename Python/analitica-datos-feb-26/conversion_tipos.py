numero_string = 'gratis'
print( type(numero_string) )

try:
    numero = float(numero_string)
    print(numero)
    print(type(numero))
except ValueError:
    print(0.0)

numero_float = 67.03

print( str(numero_float) )


precio = "39.90"

print( float(precio) )


stock = float('10.30')
print(int(stock))


