# Una función tiene dos partes - la una sin la otra no pueden convivir.

# Error no se puede ejecutar una funcion antes de la declaración
# despedir()
# parte 1: DECLARACIÓN - DEFINICIÓN

def saludar():
    print('Hola desde una funcion')
    
def despedir():
    print('vete a tu casa')
    
# parte 2: Ejecución  
for i in range(1000):
    saludar()

despedir()