class Cargo: 
    secuen = 0
    def __init__(self,des= " Sin cargo alguno" ): #*estructura de datos o atributos
        Cargo.secuen = Cargo.secuen + 1 
        self.codig = Cargo.secuen
        self.descripcion = des
if __name__=="__main__":
    #*primer caso
    Cargo1 = Cargo()
    print(Cargo1.codig,Cargo1.descripcion)
    #*segundo caso
    Cargo2 = Cargo()
    Cargo2.descripcion = " Supervisor"
    print(Cargo2.codig,Cargo2.descripcion)
    #*tercer caso
    Cargo3 = Cargo (" Analista")
    print (Cargo3.codig,Cargo3.descripcion)
    # print(Cargo.secuen)
    # print(Cargo1.secuen)
    # print(Cargo2.secuen)
    # print(Cargo3.secuen)
        