# Definir el valor de una variable en función de una condición

estado_luz = True

if estado_luz:
    mensaje = "La luz está encendida"
else: 
    mensaje = "La luz está apagada"

mensaje = "luz encendida" if estado_luz else "luz apagada"

print(mensaje)