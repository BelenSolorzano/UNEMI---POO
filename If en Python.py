#ESTRUCTURAS DE CONTROL DE PYTHON - IF
valor = int(input("Ingrese un número entero: "))
if valor < 0:
    valor = 0
    print('Negativo cambiado a cero')
elif valor == 0:
    print('El numero es cero')
elif valor == 1:
    print('El numero es uno')
else:
    print('No existe')
print("Gracias")if type(valor) == int else print ("-")