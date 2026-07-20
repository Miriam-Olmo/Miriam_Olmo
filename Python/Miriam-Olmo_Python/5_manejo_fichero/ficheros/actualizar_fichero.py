def actualizar_datos(ruta, nombre):
    fichero = open(f"{ruta}{nombre}" , "a", encoding='UTF-8')
    nombre = input('Dime el nombre del alumno: ')
    nota = input('Dime la nota del alumno: ')
    fichero.write(f"{nombre}: {nota}\n")
    fichero.close()


actualizar_datos('./datos/','notas_python.txt')
