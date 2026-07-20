# =============================================================================
# EJERCICIO 2: CATÁLOGO DE PELÍCULAS
# Tienes una lista de diccionarios con películas (titulo, director, año, nota).
# Recorre la lista y muestra cada película con sus datos formateados si la nota es aprobada en verde y si no en rojo solo la nota
# Muestra solo las películas con nota >= 8.
# Ordena la lista por año (ascendente) y muéstrala de nuevo.
# =============================================================================

peliculas = [
    {'titulo': 'El Padrino', 'director': 'F. Coppola',   'anio': 1972, 'nota': 9.2},
    {'titulo': 'Interstellar','director': 'C. Nolan',     'anio': 2014, 'nota': 8.6},
    {'titulo': 'El Gran Lebowski','director': 'Coen Bros.',   'anio': 1998, 'nota': 7.9},
    {'titulo': 'Pulp Fiction','director': 'Q. Tarantino', 'anio': 1994, 'nota': 4.9},
    {'titulo': 'La La Land','director': 'D. Chazelle',  'anio': 2016, 'nota': 3.0},
    {'titulo': 'Joker','director': 'T. Phillips',  'anio': 2019, 'nota': 7.5},
]

peliculas2 = [
    {'titulo': 'Notting Hill', 'director': 'Roger Michell', 'anio': 1999, 'nota': 9.2},
    {'titulo': 'El diario de Noa', 'director': 'Nick Cassavetes', 'anio': 2004, 'nota': 8.6},
    {'titulo': 'Tienes un email', 'director': 'Nora Ephron', 'anio': 1998, 'nota': 7.9},
    {'titulo': 'Cómo perder a un chico en 10 días', 'director': 'Donald Petrie', 'anio': 2003, 'nota': 4.9},
    {'titulo': 'Mejor... imposible', 'director': 'James L. Brooks', 'anio': 1997, 'nota': 3.0},
    {'titulo': 'Love Actually', 'director': 'Richard Curtis', 'anio': 2003, 'nota': 7.5},
]

def colorear(numero):
    rojo = "\033[91m"
    verde = "\033[92m"
    reset = "\033[0m"
    if numero >= 5 and numero <=10:
        return f"{verde}{numero}{reset}"
    elif numero >= 0 and numero < 5:
        return f"{rojo}{numero}{reset}"

def pintar_peliculas(lista_peliculas, titulo):
    print(f"\n######## {titulo} ###########\n")
    for pelicula in lista_peliculas:
        print(f"{pelicula['titulo']}  | Año: {pelicula['anio']} | Director: {pelicula['director']} | Nota: {colorear(pelicula['nota'])}")
        print('-' * 60)


#pintar_peliculas(peliculas, 'Acción')
#pintar_peliculas(peliculas2, 'Románticas')

def filtrar_por_nota(peliculas, nota_min, nota_max):
    lista_filtrada = []
    for pelicula in peliculas:
        if pelicula['nota'] >= nota_min and pelicula['nota'] <= nota_max:
            lista_filtrada.append(pelicula)
    return lista_filtrada   


#peliculas_nota_suspensa = filtrar_por_nota(peliculas2, 0, 5)
#pintar_peliculas(peliculas_nota_suspensa, 'Peliculas suspensas')


# paso 1: recorrer la lista
# paso 2: saber la condicion que encuentra lo que busco
# paso 3: meterlo en una lista nueva


def ordenar(peliculas, ordenacion):
    booleano = True if ordenacion == 'dsc' else False
    resultado = sorted(peliculas, key=lambda pelicula: pelicula['anio'], reverse=booleano)
    return resultado

peliculas_ordenadas = ordenar(peliculas2, 'dsc') # 'dsc"
pintar_peliculas(peliculas_ordenadas, 'Peliculas ordenadas')