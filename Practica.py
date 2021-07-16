#clase full encapsulada. 
class Logica:
    def __init__(self, lista = None):
        self.__lista = lista
    
    @property
    def lista(self):
        return self.__lista 
    @lista.setter
    def lista(self,value):
        self.__lista = value 

    def parImpar(self,numero):
        reci = numero % 2 
        if reci == 0 :
            print (" El numero {} es par ".format(numero))
        else:
            print (" El numero {} es impar ".format(numero))

    def perfecto(self, nu):
        conta, acum = 1,0
        for conta in range (1,nu):
            reci = nu % conta
            if reci == 0 :
                acum = acum + conta
        if acum == nu:
            print("EL numero {} es perfecto".format(nu))
        else: 
            print("EL numero {} no es perfecto".format(nu))


    # # def divisores(self, mumero):
    #     pass 

class Ejercicio (Logica):
    def __init__(self,lista,numero):
        super().__init__(lista)
        self.datos = numero

    def suma (self,n1,n2):
        return n1 + n2  
    
    def parImpar(self,numero): 
        super().parImpar(numero)
        return numero % 2 
      
ejer = Ejercicio([3,6,9],12) 
numer = int(input(" Ingrese un numero: "))
ejer.perfecto(numer)
# ejer.parImpar (5)
# if ejer.parImpar(6)== 0 :
#     print (" El numero es par ")
# else:
#     print (" El numero es impar ")
# print(ejer.lista)
# print( ejer.suma (35,12))
# ejer = Logica([3,6,9]) 
# numer = int(input(" Ingrese un numero: ")) 
# ejer.parImpar (numer)