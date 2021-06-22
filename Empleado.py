from cargos import Cargo 
class Empleado:
    secuen = 0 
    def __init__(self,nom, cedu, suel, Cargos):
        self.codig = self.generCodig()
        self.nombre = nom
        self.cédula = cedu
        self.sueldo = suel
        self.cargo = Cargos
    def presentar(self):
        print("Código: {} Nombre: {} Cargo: {} - {}".format(self.codig,self.nombre,self.cargo.codig,self.cargo.descripcion))
    def generCodig (self):
        Empleado.secuen = Empleado.secuen + 1
        return Empleado.secuen 
Cargo1 = Cargo("Supervisor")
emp1 = Empleado("Javier","0911",450,Cargo1)
emp1.presentar()
Cargo2 = Cargo (" Analista")
emp2 = Empleado("Felipe","1345",700,Cargo2)
emp2.presentar()