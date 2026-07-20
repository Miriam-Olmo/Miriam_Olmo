# definir el valor de una variable en funcion de una condicion

estado_luz = True

if estado_luz:
    mensaje = 'luz encendida'
else:
    mensaje = 'luz apagada'

mensaje = 'luz encendida' if estado_luz else 'luz apagada'

print(mensaje)