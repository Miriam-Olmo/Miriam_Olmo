def limpiar_id(id):
    # si no hay id
    if not id:
        return None
    id = str(id).strip()
    return int(id)


def limpiar_texto(valor, mayusculas = False):
    if not valor:
        return 'Sin datos'
    valor = str(valor).strip()
    return valor.upper() if mayusculas else valor.lower()


def limpiar_precio(valor):
    lista_monedas = ['€', '$']
    if not valor: 
        return 0.0
    precio_txt = str(valor).strip().replace(',', '.').lower()
    for moneda in lista_monedas:
        precio_txt = precio_txt.replace(moneda, '')
    try:
        return round(float(precio_txt), 3)
    except ValueError:
        return 0.0
    
    
def limpiar_stock(valor):
    if not valor:
        return 0
    stock_txt = str(valor).strip()
    try:
        stock_num = float(stock_txt)
        return 0 if stock_num < 0 else int(stock_num)
    except ValueError:
        return 0