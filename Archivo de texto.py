archivo, f = "alumno.txt", " "
alumnos = [{"Nombre": "Felipe",  "Edad": 21, "fac":"Derecho"},
           {"Nombre": "Mathias", "Edad": 20, "fac":"Economia"},
           {"Nombre": "César",   "Edad": 23, "fac":"Ingeniería"}]

# Escribir archivos: w - a: write - writeline

with open (archivo, "w") as write: 
    for i in range ( len(alumnos)):
        linea = " "
        for clave, valor in alumnos [i].items():
            if clave == "fac":
                linea = linea + (str(valor) if type(valor) == int else valor) + "\n" 
            else:
                linea = linea + (str(valor) if type(valor) == int else valor) + ";"  
            write.writelines(linea)

#* Leer archivos: r : read - readline - redlines - in 

try:
    f = open (archivo, "r")
    for linea in f :
        print (linea[:-1])
except Exception as e: 
    print ("Error de archivo: " + str(e))
finally:
    f.close()    