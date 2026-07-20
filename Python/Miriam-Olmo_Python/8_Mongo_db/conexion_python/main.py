from controllers.sismos_controller import get_all, get_by_city, insert_sismo, get_by_id, delete_sismo, filter_by_magnitude, update_sismo
import pandas as pd

def init():
    menu = """APP Control de Sismos
[1]. Lista sismos
[2]. Buscar un sismo por lugar
[3]. Dar de alta un sismo
[4]. Eliminar un sismo
[5]. Actualizar un sismo
[6]. Filtrar sismos por magnitud
[x]. Salir    
    """
    print(menu)
    print('=' * 30)
    option = input('Dime que opción seleccionas: ')
    print(option)
    # crear un condicional que me permita entrar en cada opcion y mantenerme dentro la app hasta pulsar salir.
    if option == '1':
        
       result = get_all(30)
       df = pd.DataFrame(result)
       print(df[['lugar', 'magnitud','profundidadKm', 'fechaHora']])
       
    elif option == '2':
        
        lugar = input('Dime de que lugar quieres el sismo: ')
        result = get_by_city(lugar)
        df = pd.DataFrame(result)
        print(df[['lugar', 'magnitud', 'fechaHora']])
        
    elif option == '3':
        try:
            new_sismo = {
                "lugar":input('Dime el lugar del sismo: '),
                "fechaHora":input('Introduce la fecha y hora del sismo: DD/MM/YY HH:MM:SS: '),
                "magnitud": float(input('Magnitud del sismo: ')),
                "profundidadKm":float(input('Dame la profundidad en km: '))
            }
            result = insert_sismo(new_sismo)
            print(result)
        except ValueError:
            print('la magnitud y y profundidad son numericas')
            init()   
    elif option == '4':
        id = input('Dime el ID del sismo a eliminar: ')
        result = delete_sismo(id)
        print(result) 
    elif option == '5':
    # tenemos que preguntar el sismo que queremos actualizar por ID.
        id_sismo = input('Dime el sismo que quieres actualizar: ')
        sismo = get_by_id(id_sismo)
        print(f"Lugar actual: {sismo['lugar']} , magnitud actual: {sismo['magnitud']}")
        actualizar = input('Deseas actualizar este sismo: si o no: ')
        if actualizar == 'no':
            print('no se ha actualizada nada')
            init()
        print('Si no quieres actualizar un campo, dale Enter')

        datos_actualizar = {}

        magnitud = input('Dime la magnitud del sismo: ')
        if magnitud != '':
            datos_actualizar['magnitud'] = float(magnitud)

        profundidad = input('Dime la profundidad del sismo: ')
        if profundidad != '':
            datos_actualizar['profundidadKm'] = float(profundidad)

        result = update_sismo(id_sismo, datos_actualizar)
        print(result)
    elif option == '6':
        try:
            magnitud = float(input('Dime la magnitud del sismo: '))
            result = filter_by_magnitude(magnitud)
            df = pd.DataFrame(result)
            print(df[['lugar', 'magnitud', 'fechaHora']])
        except ValueError:
            print('La magnitud tiene que se numero')
            
    elif option.lower() == 'x':
        print('Hasta pronto')
        return 
    else:
        print('opción seleccionada no valida')
    
    init() 
        
if __name__ == '__main__':
    init()