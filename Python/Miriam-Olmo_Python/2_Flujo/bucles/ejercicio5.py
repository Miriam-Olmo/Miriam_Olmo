# """"""


# ** 
# ****
# ******
# ********
# **********
# ************
# **************
# *
# *
# ----


#pedimos el numero de asteriscos al usuario
asteriscos = int(input('dime el numeros de asteriscos: '))

# parte que sube desde 1 hasta asteriscos

for i in range(1, asteriscos + 1):
    print( "*" * i)

# parte que baja

for i in range(1, asteriscos,0 -1):
    print("*" * i)