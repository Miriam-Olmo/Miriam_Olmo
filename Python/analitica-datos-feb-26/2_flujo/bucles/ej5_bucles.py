"""

*
**
***
****
*****
******
*******
********
*******
******
*****
***
**
*

"""

# pedimos el numero de asteriscos al usuario
asteriscos = int(input('Dime el número máximo de asteriscos: '))

# parte que sube vamos desde 1 hasta asteriscos
for i in range(1, asteriscos + 1):
    print("*" * i)
    
    
# parte que baja 
for i in range(asteriscos + 1,0, -1):
    print("*" * i)

