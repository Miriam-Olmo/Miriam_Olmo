# me permite mayor rango de cambios en el desarrollo del bucle.


# for i in range(1, 10):
#     print(i)
  
j = 1 
while j <= 10:
    j = j + 1
    print(j)
    if j % 2 != 0:
        break
else:
    print('he terminado el bucle')