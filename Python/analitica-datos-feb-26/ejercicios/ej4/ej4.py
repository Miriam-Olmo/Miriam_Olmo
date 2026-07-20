from data.trabajadores import trabajadores

def calcular_coste_hora_extra(trabajador):
    # dividimos el sueldo por las horas y sacamos el coste hora
    coste_hora_extra = trabajador['sueldo_base'] / trabajador['horas_contrato']
    # multiplicamos por las horas extra, y obtenemos el coste_horas_extra
    total_horas_extra = coste_hora_extra * trabajador['horas_extra']    
    # se lo añadimos al trabajo clave: valor
    trabajador['total_horas_extra'] = total_horas_extra

## calcular la nomina de un trabajador

def calcular_nomina(trabajador):
    irpf = trabajador['sueldo_base'] * (trabajador['porcentaje_impuestos']/100)
    sueldo_neto_sin_extras = trabajador['sueldo_base'] - irpf
    sueldo_final = sueldo_neto_sin_extras + trabajador['total_horas_extra']
    trabajador['nomina'] = sueldo_final

## calcular la nomina de todos los trabajadores.
## calcular los horas extra de todos los trabajadores.
for trabajador in trabajadores:
    calcular_coste_hora_extra(trabajador)
    calcular_nomina(trabajador)
    

### pintar todos los trabajadores de la lista.
def mostrar_trabajadores(lista_trabajadores):
    for trabajador in lista_trabajadores:
        print('-'* 30)
        print(f"{trabajador['nombre']} - {trabajador['departamento']}")
        print('-'* 30)
        
#mostrar_trabajadores(trabajadores)

### filtrar los trabajadores y pintarlo por categoria


def filtrar_por_departamento(lista_trabajadores, departamento):
    lista_filtrada = []
    for trabajador in lista_trabajadores:
        if trabajador['departamento'] == departamento:
            lista_filtrada.append(trabajador)
    return lista_filtrada

lista_direccion = filtrar_por_departamento(trabajadores, 'Dirección')
lista_marketing = filtrar_por_departamento(trabajadores,'Marketing')

mostrar_trabajadores(lista_direccion)