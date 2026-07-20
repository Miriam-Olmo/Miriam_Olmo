print('-- simulacion de conexion a BBDD')

conexion_bbdd = False
lista_inexistente = ['uno', 'dos']
try:
    print('1 - conectando a la bbdd')
    conexion_bbdd = True
    print('2- pedimos los datos de un cliente')
    clientes = lista_inexistente[2]
    print('cliente encontrado')
except NameError:
    print('la tabla de cleintes no existe')
except IndexError:
    print('el cliente no existe')
finally:
    print('cierro la conexion')

print('lo siguiente')