# es un conjuntos de datos donde se pierde el factor posicion, los vamos referenciar por clave. Teniendo un conjunto clave:valor

alumno = {
    'nombre': 'Juan Antonio', 
    'edad': 44,
    'tlf': 677788899
    }

# print(alumno) imprime el diccionario por pantalla
# obtenemos el valor poniendo su clave asociada
print(alumno['nombre']) # Juan Antonio

# getters
print( alumno.get('edad') ) # 44

alumno['tlf'] = 644563456
alumno['direccion'] = 'Calle Fray Luis de Leon'

print(alumno)

# eliminar
alumno.pop('direccion') # eliminamos esa clave con su valor.

# diccionario complejo
producto = {
    'titulo': 'Portatil HP',
    'precio': 1200,
    'caracteristicas' : {
        'ram': 16,
        'procesador': 'AMD RYZEN 7',
        'disco': [256, 512]
    },
    'pantalla': ['1920', '1980']
}

# resolucion pantalla horizontal
print( producto['pantalla'][0] ) # 1920
# ram
print( producto['caracteristicas']['ram'] )
# discos 
print('---------')
for i in range(len(producto['caracteristicas']['disco'])):
    print(producto['caracteristicas']['disco'][i])

# podemos extraer todos lo elementos
for valor in alumno.values():
    print(valor)

print("----------")
# podemos extraer todas las claves
for clave in alumno.keys():
    print(clave)
    
print("----------")

# podemos extraer todas las claves con sus elementos
for clave, valor in alumno.items():
    print( f"{clave}: {valor}" )
    
print( alumno.values() )
print( alumno.keys())
print( alumno.items())




