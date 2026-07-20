def comprobar_duplicados(email, tel, lista):
    ## tenemos que recorrer la lista buscando un registro que tenga o el email o el telefono, si esto ocurre devolvemos False
    for contacto in lista:
        if contacto['email'] == email or contacto['telefono'] == tel:
            return False
    # si no hay nada devolvemos True por que no hay duplicados
    return True
    


def insertar_contacto(nombre, email, tel, lista):
    # aqui todos los datos son correctos
    # crear el diccionario
    nuevo_contacto = {
        'nombre': nombre,
        'email': email,
        'telefono': tel
    }
    no_duplicado = comprobar_duplicados(email, tel, lista)
    # insertarlo en la agenda, no puede ocurrir append si el email o el telefono ya existe en la agenda
    if no_duplicado:
        lista.append(nuevo_contacto)
    else:
        print('Usuario duplicado')
    
def validar_contacto(nombre, email, tel):
    if nombre == "" or not tel.isdigit() or '@' not in email:
        return False
    return True

def pintar_contactos(lista):
    for contacto in lista:
        print("-"*30)
        print(f"{contacto['nombre']} - {contacto['email']} - {contacto['telefono']}")
        print("-"*30)