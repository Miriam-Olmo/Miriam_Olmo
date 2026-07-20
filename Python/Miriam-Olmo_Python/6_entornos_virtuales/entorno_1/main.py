import requests as rq
from colorama import init, Fore
## consulta a la api del tiempo y devolvernos los dato de tiempo y temperatua de un ciudad cualquiera
init()

def obtener_temperatura(ciudad):
    url= f"https://wttr.in/{ciudad}?format=j2"
    # la libreria requests me permite hacer una peticion a cualquier url
    # una API responde al siguien patron
    #      VERBO - URL 
    #      GET - SELECT -  https://wttr.in/madrid obtener los datos de temperatua de madrid
    # POST - Crear - INSERT
    # PUT - Actualizar - UPDATE
    # DELETE - Borrar - DELETE
    respuestaApi = rq.get(url)
    ## viene comprimida la descomprimo con .json()
    data = respuestaApi.json()
    temperatura = data['current_condition'][0]['temp_C']
    humedad = data['current_condition'][0]['humidity']
    descripcion = data['current_condition'][0]['weatherDesc'][0]['value']
    color = Fore.BLUE if float(temperatura) < 25 else Fore.RED
    temperatura_color = color + str(temperatura) 
    
    print(f"La temperatura de {ciudad.title()} es {temperatura_color} ºC {Fore.RESET}, el porcentaje de humedad es de {humedad}% y el día en general es {descripcion}")
    
# quiero que me pidais por pantalla una ciudad , la paseis a minuscula y ejecuteis la funcion a ver que sale
ciudad = input('dame un ciudad: ').lower()
obtener_temperatura(ciudad)
