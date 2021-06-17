class For:
    def __init__(self):
        pass 
      # ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero (mientras tengo valores)
    def usoFor(self):
        nombre = " Marcos"
        datos = ["Marcos", 28 , True]
        numeros = (2,5.6,4,1)
        docente = {'Nombre': 'Marcos', 'Edad':28 , 'Fac': 'Faci'}
        listNotas = [(40,40),(35,40),(50,45)]
        listAlumnos = [{"Nombre":"Alex","Nota":80},{"Nombre":"Luci","Nota":75},{"Nombre":"Felix","Nota":95}]
        #? range([inicio = 0, limite,[inc/dec = 1].Genere un rango de valores desde un valor inicial a un valor final])
        #! se ejecuta desde inicio hasta el limite
        # for i in range(5): # rango (0,1,2,3,4)  
        #     print("i={}".format(i))
        # for i in range(2,10): # rango (2,3,4,5,6,7,8,9)  
        #     print("i={}".format(i)) 
        # for i in range(4,10,2): # rango (4,6,8,)  
        #     print("i = {}".format(i),   end = "  ") 
        # for i in range(12,3,-3): # rango (4,6,8,)  
        #     print("i={}".format(i),   end = "  ")
        
        # longitud = len (datos)  #len funciona en lista, tuplas y diccionarios
        # print(datos[0])
        # print(datos[1]) 
        # print(datos[2])

        # for i in range(longitud-1,-1,-1):
        #     print("for", datos[i]) 

        # for i , dato in enumerate(datos): #aplicables solo para lsita y tuplas
        #     print("for",i, dato)
        #Dato Toma cada elemento de la coleccion numeros ( cadena , lista , tupla)
        # for dato in numeros:
        #     print(dato) 
        # for dato in ["H","o","l","a","que","tal"]:
        #     print(dato)

        # print("\nDcicionario de nota")
        # # for clave , valor in docente,items():
        # #     print(clave;":", valor,end = " ")  

        # for docente in listAlumnos:
        #     for clave , valor in docente.items():
        #         print(clave,":", valor,end = " ")  

        # Sacar primedios por cada alumno
        # listNotas = [(40,40),(35,40,60),(50,45,34,45,40)]  
        # acum = 0 
        # long = 0 
        # for notas in listNotas:  #ciclos anidados
        #     # print(notas) 
        #     acuParcial = 0 
        #     for nota in notas:
        #         print(nota)
        #         long=long + 1 
        #         acum = acum + nota
        #         acuParcial = acuParcial + nota  
        #     promParcial = acuParcial /len(notas)
        #     print("Notas Parciales = {} Pormedio Parcial = {}".format(acuParcial,promParcial))
        # prom = acum/long
        # print("Total notas = {} - #Notas = {} :Promedio = {} ".format(acum,long,prom))
        #     listAlumnos = [{"Nombre":"Alex","Nota":80},{"Nombre":"Luci","Nota":75},{"Nombre":"Felix","Nota":95}]
        #    #Sacar promedio general de un grupo de alumnos
        #     acum = 0 
        #     cont = 0 
        #     for alumnos in listAlumnos:
        #         print(alumnos)
        #         cont += 1 
        #         for i, va in alumnos.items():
        #             print(i," : ", va , end= " ")
        #             if i  == "Nota": acum = acum + va
        #     print (acum / cont)
        # palabra = " Bienvenido a mi cumpleaños"
        # #presentar poor lista las vocales
        # vocales = []
        # for carac in palabra:
        #     if carac in ("a","e","i","o","u"):
        #         vocales.append(carac)
        # print(vocales)
        #segunda forma
        print ([carac for carac in " Bienvenido a mi cumpleaños" if carac in ("a","e","i","o","u") ]) #comprension
       
bucle1 = For()
bucle1.usoFor()