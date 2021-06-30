class Operaciones: 
    def __init__(self,nu1, nu2):
        self.número1 = nu1 
        self.número2 = nu2
    
    def Suma(self): #método
       Suma = self.número1 + self.número2
       return Suma

    def Resta(self):
        if self.número1 - self.número2 :
            return self.número1 - self.número2 
        return 0 

    def Multiplicación(self):
        return self.número1 * self.número2  

    def División (self):  
        print(self.número1 / self.número2) 

    def División_Entera (self):
        if self.número2 != 0 : return self.número1 // self.número2
        return 0 

    def Residuo(self):  
        print(self.número1 % self.número2)

    def Exponente(self):
        return self.número1 ** self.número2  

    def Mostrar(self):
        print("operan1 = {}, operan2 = {}".format( print(self.número1, self.número2)))

# oper = Operaciones(10,20) 
# x = oper.sum
# # print(operac.Suma())
# # print(operac.División()) 
# y = oper.Resta()
# z = x ** y
# print(z) 
# oper.mostrar()
print("Menú de Operaciones Matemáticas\n----------------------------------")
print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. División entera\n6. Residuo\n7. Exponente\n8")
opcción = "0"
while opcción != "8":
    opcción = input("Elija una opcion[1...8]: ")
    if opcción == "1":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("La suma de {} + {} es = {}".format(op.número1,op.número2,op.Suma()))
    elif opcción == "2":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("La resta de {} - {} es = {}".format(op.número1,op.número2,op.Resta()))
    elif opcción == "3":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("La multiplicación de {} * {} es = {}".format(op.número1,op.número2,op.Multiplicación()))
    elif opcción == "4":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("La división de {} / {} es = {}".format(op.número1,op.número2,op.División()))
    elif opcción == "5":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("La división entera de {} // {} es = {}".format(op.número1,op.número2,op.División_Entera()))
    elif opcción == "6":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("El residuo de {} % {} es = {}".format(op.número1,op.número2,op.Residuo()))
    elif opcción == "7":
        nu1 = int(input(" Ingrese número 1 : ")) 
        nu2 = int(input(" Ingrese número 2 : "))
        op = Operaciones(nu1,nu2)
        print("El exponente de {} ** {} es = {}".format(op.número1,op.número2,op.Exponente()))
    else: 
        print ("Fin de proceso")







