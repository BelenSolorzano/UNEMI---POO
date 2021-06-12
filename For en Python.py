# ESTRUCTURAS DE CONTROL DE PYTHON - FOR
#for range (v) - range(vi,vf) - range(vi,vf,inc)
letras = input("Ingrese frase: ")
for contar in range(len(letras)):
    print(contar,'=',letras[contar])
#for in cadena - in (tupla) - in[lista]
conVocales=0
for vocal in letras:
    if vocal in ("a","e","i","o","u","A","E","I","O","U"):
        if vocal in["A","E","I","O","U"]:
            continue
        else:
            conVocales = conVocales + 1
print('La cantidad  de vocales encontradas es:{}'.format(conVocales))
#Comprehension - [var for var in datos condition]
[vocal for vocal in['a','e','i','o','u']if vocal not in ('a','i','o',)]