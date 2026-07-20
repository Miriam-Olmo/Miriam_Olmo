print('-- Simulacion de conexion a BBDD')

conexion_bbdd = False
lista_inexistente = ['uno','dos', 'tres']
try:
    print('1 - conectando a la BBDD')
    conexion_bbdd = True
    print('2 - pedimos los dato de un cliente')
    cliente = lista_inexistente[2]
    print('cliente encontrado')
except NameError:
    print('la tabla de clientes no existe')
except IndexError:
    print('El cliente solicitado no existe')
finally:
    print('cierro la conexion')
    

print('lo siguiente')