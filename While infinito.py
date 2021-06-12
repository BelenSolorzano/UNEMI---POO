# ESTRUCTURAS DE CONTROL DE PYTHON - WHILE
'''uso de while infinito'''
c= 1
while True:
    print(c)
#while validación  _ Para ejercutar las demas lineas comentar las anteriores.
vocal = input("Ingrese vocal:")
while vocal not in ('a','e','i','o','u'):
    if vocal == '.':
        break
    vocal = input("Vocal:")
print('Su vocal o punto es :{}'.format(vocal))