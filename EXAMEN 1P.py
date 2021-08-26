
#* Pregunta 1:
#? Dado el siguiente método find_encontrar() de la clase Cadena. El método tiene que retornar la posición
#? de un caracter buscado en la cadena. 
#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Cadena():
#     def __init__(self,cadena):
#         self.cadena = cadena
#         self.__listaMinúscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         self.__listaMayúscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#     def find_encontrar(self,buscar):
#         for i,v in enumerate(self.cadena):
#             if v == buscar:
#                 return i      #el error era : return v 
#         return -1  
# cad= Cadena()
# print(cad.find_encontrar(Cadena)) 


#* Pregunta 2:
#? Dado el siguiente método invertirCadena() de la clase Examen. El método recibe como parámetros una cadena. El método tiene que retornar
#? la cadena recibida como parámetro de manera invertida. Ejemplo:
    # exa = Examen()
    # print(exa.invertirCadena("daniel"))
    # respuesta = "leinad"

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Examen: 
#     def __init__(self,lista=[]):
#         self.lista=lista
#     def invertirCadena(self,cadena):
#         invertida=""
#         cont=len(cadena)
#         indice= -1
#         while cont >=1: 
#             invertida +=cadena[indice]       
#             indice = indice - 1              #el error era : indice + 1
#             cont -=1
#         return invertida
# exa = Examen()
# print(exa.invertirCadena("daniel")) 

#* Pregunta 3: 
#? Dada al siguiente lista:
# listaFrase=["hola","Daniel","Vera","que","tal","como","estas","en POO"]
# Seleccione la alternativa de código correcta para obtener la siguiente
#  listaFrase2=['hola', 'Daniel', 'que', 'tal', 'en POO'] 

## listaFrase2= listaFrase[0:2] + listaFrase[3:4] + listaFrase[7:]
#! listaFrase2= listaFrase[:2] + listaFrase[3:5] + listaFrase[7:]         # respuesta
## listaFrase2= listaFrase[0:2] + listaFrase[3:4] + listaFrase[7:-1]
## listaFrase2= listaFrase[2] + listaFrase[3:5] + listaFrase[7:-1] 

#* Pregunta 4: 
#? Dada el siguiente método decimalBinario() de la clase Ejercicios
# El método tiene que retornar un número binario a partir de un número cedimal:
# Ejemplo:
   # ejer = Ejercicio()
   # print(ejer.decimalBinario(5))
   # respuesta = 101
#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente
# class Ejercicios:
#     def decimalBinario(self, decimal):
#         binario = " "
#         while decimal //2 != 0:
#             binario = str (decimal % 2) + binario
#             decimal = decimal // 2 
#         return str(decimal)+ binario 
# ejer = Ejercicios()
# print(ejer.decimalBinario(5))

#* Pregunta 5: 
#? El siguiente código guarda en un diccionario en la clave "pares" una lista de números pares
#? y en la clave "impares" guarda en una lista los numeros impares

# class Calculos:
#     def __init__(self, numero):
#         self.numero = numero
    
#     def paresEimpares(self):
#         dicc = {"Pares":[],"Impares":[]}
#         for num in range(self.numero):
#             if num % 2 == 0:
#                 dicc["Pares"].append (num)
#             else:
#                 dicc["Impares"].append (num)
#         return dicc 
# di = Calculos(9)
# print(di.paresEimpares()) 

#* Pregunta 6: 
#? El siguiente método realiza el cálculo de un número factorial: El factorial de un número resulta
#? de multiplicar todos los números enteros que hay entre ese número y el 1 
# ejemplo: 
     # 4! = 4 * 3 * 2 * 1 = 24 

# def facto_1(n):
#     factoral_total = 1
#     while n > 1 :
#         factoral_total *= n
#         n -= 1            #! estaba fuera de la linea de la lógica
#     return factoral_total
# print(facto_1(6)) 

#* Pregunta 7: 
#? Dado el siguiente método insertarPos() de la clase ordenar
#? El método tiene que insertar un valor en la posición indicada
# Ejemplo:
   # lista = [2,3,8,10,3]
   # ord1 = Ordenar(lista)
   # ord1.insertPos(2,20)
   # respuesta = [2,3,20,8,10,3]
   # lista = [2,3,10,3]
   # ord1.insertPos(5,20)
   # respuesta = [2,3,8,10,3,20]

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Ordenar:
#     def __init__(self, lista):
#         self.lista = lista
     
#     def insertarPos (self, pos, valor):
#         auxlista = []
#         if len(self.lista) == pos:
#             self.lista.append(valor)
#         else:
#             for indice, ele in enumerate(self.lista):
#                 if indice == pos:
#                     auxlista.append(valor)
#                 auxlista.append(ele)
#             self.lista = auxlista
#         return self.lista  
# lista = [2,3,8,10,3]
# ord1 = Ordenar(lista)
# print(ord1.insertarPos(2,20)) 
#respuesta = [2,3,20,8,10,3]
#lista = [2,3,10,3]
#ord1 = Ordenar(lista)
#print(ord1.insertarPos(5,20))
#respuesta = [2,3,8,10,3,20]  

#* Pregunta 8: 
#? Dada el siguiente método mayMin() de la clase Cadena
#? El método tiene que retornar una tupla con la cantidad de mayúsculas y minúsculas de una cadena:
# Ejemplo:
  # tarea = Cadena ("Examen de POO")
  # print(tarea.mayMin())
  # respuesta = (4,7) 

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Cadena():
#     def __init__(self,cadena):
#         self.cadena = cadena
#         self.Minúscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#         self.Mayúscula = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
#     def mayMin(self):
#         cmay,cmin = 0,0
#         for i , v in enumerate(self.cadena):
#             if v in self.Mayúscula:
#                 cmay += 1
#             elif v in self.Minúscula:
#                 cmin += 1
#         return print("Cantidad de mayúsculas:{}" "\n" "Cantidad de minúsculas:{}".format(cmay,cmin))
# tarea = Cadena ("Examen de POO")
# print(tarea.mayMin())

#* Pregunta 9: 
#? Dada el siguiente método ListaMenor() de la clase Examen
#? El método tiene que retornar una lista de todos los números menores a un npumero que se recibe como parámetro.
#  exa = Examen([2,5,20,16])
#  print(exa.ListaMenor(13))
#  respuesta = [2,5] 

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Examen: 
#     def __init__(self,lista=[]):
#         self.lista = lista 

#     def ListaMenor(self, num):
#         listamenor = []
#         for menor in self.lista:
#             if menor < num:
#                 listamenor.append(menor) 
#                 return listamenor       
# exa = Examen ([2,5,20,16])
# print(exa.ListaMenor(13)) 

#* Pregunta 10:
#? Dada el siguiente método listaMultiplo() de la clade Examen
#? El método recibe como parámetro un número. El método tiene que retornar uan lista de todos los 
#? elementos del atributo lista de la clase que son múltiplos del parámetro numero del método.
# Ejemplo:
  # exa = Examen ([2,5,8,10,20])
  # print(exa.ListaMultiplo(5)) 
  # respuest = [5,10,20] 

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente
# class Examen: 
#     def __init__(self,lista=[]):
#         self.lista = lista 

#     def ListaMultiplo(self, numero):
#         lista = []
#         for num in self.lista:
#             if not (num % numero != 0 ):
#                 lista.append(num)
#         return lista     
# exa = Examen ([2,5,8,10,20])
# print(exa.ListaMultiplo(5))  

#* Pregunta 11: 
#? El siguiente código comprueba si un número ingresado es un número abundante: se dice que un número es abundante ,
#? cuando la suma de sus divisores incluido el 1 y excluido el propio número es mayor que él.
# Ejemplo:
# número 30 es abundante poruqe sus divisores son: 1,2,3,5,6,10,15 suman 42 que es mayor que 30

# def numero_abundante(n):
#     cont = 1 
#     suma = 0 
#     while (cont < n):
#         if (n % cont == 0):
#             suma += cont
#         cont = cont + 1
#     if (suma > (n)):
#         return True
#     else:
#         return False
# print(numero_abundante(12))

#* Pregunta 12: 
#? El siguiente código verifica si una frase es palindroma. Una frase es palindroma si se lee de igual forma de derecha
#? a izquierda como de izquierda a derecha.
# Por ejemplo: anita lava la tina. 

#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Cadena:
#     def __init__(self, cad= ""):
#         self.cadena = cad
    
#     def palindroma(self,original=""):
#         invertir = self.cadena[::-1]
#         invertir = invertir.replace(" ", "")
#         original = self.cadena.replace(" ", "")
#         if original.lower() == invertir.lower():
#             return "Palindroma"
#         else:
#             return " No es palindroma" 
# pa = Cadena("anita lava la tina")
# print(pa.palindroma()) 

#* Pregunta 13: 
#? Dada el siguiente método obtenerVuelto() de la clase Vuelto
#? El método tiene que calcular el vuelto restando el pago - costo y luego este vuelto lo retomará en una lista 
#? donde cada elemento será un diccionario donde la clave será la cantidad de billetes y el valor el tipo de nominación
#? de billete de mayor a menor Numeración
# Ejemplo:
# vue = Vuleto(53,100)
# print (vue.obtenerVuelto())
# respuesta = [{2:20},{1:5},{2:1}]
  # NOTA: En este ejemplo es: 2 billetes de $20, 1 billete de $5 y 2 billetes de $1 
  # la clase funciona para dar vvueltos de entre $0 - $99  
  
#! Indique que linea o lineas estan con error y que hacen que el metodo no funcione correctamente

# class Vuelto:
#     def __init__(self,costo , pago):
#         self.__costo = costo
#         self.__pago= pago
#         self.__billetes = [50,20,10,5, 1] 
    
#     def obtenerVuelto(self):
#         vuelto = self.__pago - self.__costo
#         vueltos = vuelto 
#         for moneda in self.__billetes:
#             if vuelto >= moneda:
#                 billete = vuelto // moneda 
#                 vuelto = vuelto% moneda
#                 vueltos.append({billete:moneda})
#             return vueltos
# vue= Vuelto(54,100)
# print(vue.obtenerVuelto()) 

#* Pregunta 14: 
#? Dado el método Top de la clase ordenar.Top() devuelve el primer elemento de una colección eliminandolo de la colección.

#! Indicar si este método devuelve el valor indicado.

# class Ordenar :
#     def __init__(self,lista):
#         self.lista = lista
    
#     def top(self):
#         auxilista = []
#         for pos in range (0, len(self.lista)):
#             auxilista.append(self.lista[pos])  
#         self.lista = auxilista
#         return self.lista[0]
# li = Ordenar("Atardecer")
# print(li.top()) 
class Persona:
    _siguiente = 0
    def __init__(self,nombre="Invitado",activo=True):
        self.__codigo = self._siguiente+1
        self.__nombre = self.__nombreMayuscula(nombre)
        self.activo = activo
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre = nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo = cod
    def mostrar_datos(self):
        return "Codigo: {} - Nombre: {} - Activo: {}".format(self.codigo, self.nombre, self.activo)
    def __nombreMayuscula(self, nombre=""):
        return nombre.upper()

class Empleado(Persona):
    def __init__(self,nom='Invitado',act=True,sueldo=386):
        Persona.__init__(self,nom,act)
        self.sueldo=sueldo
    def mostrar_datos(self):
        return Persona.mostrar_datos(self)+" - Sueldo: "+str(self.sueldo)

si = Empleado()
si.mostrar_datos()