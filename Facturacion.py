from datetime import date
class Empresa:
    def __init__(self,nom="El baraton",ruc="237484011",tel="0956382617",dir="Av. las Cajas" ):
        self.nombre = nom
        self.ruc = ruc 
        self.telefono = tel
        self.direccion = dir 

    def mostrarEmpresa(self):
        print("Empresa: {:20} Ruc: {} ".format(self.nombre,self.ruc))

from abc import ABC, abstractmethod 
class Cliente(ABC):
        def __init__(self,nom,ced,tel): 
            self.nombre = nom
            self.cedula = ced  
            self.telefono = tel 

        @abstractmethod
        def getCedula(self):
            return self.cedula 

        def mostrarCliente(self):
            print(self.nombre,self.cedula, self.telefono)

class ClienteCoorporativo(Cliente): # herencia y polimorfismo  
    def __init__(self,nom,ced,tel,contrato): 
        super().__init__(nom,ced,tel) #*supper: permite accesar a los privados
        self.__contrato = contrato  

    @property  # Permite accesar al atributo privado para hacer cambios o no del mismo
    def contrato(self):          #* getter : obtener el valor del atributo privado
        return self.__contrato
    
    @contrato.setter
    def contrato(self, value):   #* setter: asigna un valor al atributo privado
        if value :    
            self.__contrato = value 
        else:
            self.__contrato = "Sin contrato"


    def mostrarCliente(self): #- se aplica polimorfismo porque hay datos que no son necesario mostrar
        print(self.nombre, self.__contrato)  
    
class ClientePersonal(Cliente): # herencia y polimorfismo  
    def __init__(self,nom,ced,tel,promocion= True): 
        super().__init__(nom,ced,tel) #*supper: permite accesar a los privados
        self.__promocion = promocion  

    @property
    def promocion(self):          #* getter : obtener el valor del atributo privado
        if self.__promocion == True:
            return " 20 % descuento"
        else:
            return "No hay Promocion"
        # return self.__promocion #! muestra dato pero no permite que el usuario cambie.

    def mostrarCliente(self): #- se aplica polimorfismo porque hay datos que no son necesario mostrar
        print("Cliente: {:13}  C??dula: {}" .format(self.nombre, self.cedula))

    def getCedula(self):
        return super().getCedula() 

class Art??culo: 
    secuencia = 0  
    iva = 0.12
    def __init__(self,des,pre,stock): 
        Art??culo.secuencia += 1
        self.c??digo = Art??culo.secuencia
        self.descripcion = des
        self.precio = pre
        self. stock = stock 
   
    def mostrarArticulo(self): #- se aplica polimorfismo porque hay datos que no son necesario mostrar
        print(self.c??digo, self.descripcion)

class DetVenta: 
    linea = 0  # atributo de clase - instancia 

    def __init__(self,articulo,cantidad) :
        DetVenta.linea += 1  # Contador de las linaes de detalles
        self.lineaDetalle = DetVenta.linea
        self.articulo = articulo 
        self.precio = articulo.precio
        self.cantidad = cantidad
     
class CabVenta: # Relacion entre entidades o clases  
    def __init__(self,fac,fecha,cliente,total= 0 ):
        #self.empresa = empresa
        self.factura = fac
        #self.nombreEmpre = empNombre # permite volverlo a mostrar las veces necesarias y cambiar a futuro.
        self.fecha = fecha
        self.cliente = cliente
        self.total = total 
        self.detalleVenta = []  
    # composici??n
    def AgregarDetalle(self,articulo, cantidad):   
        detalle = DetVenta(articulo, cantidad)
        self.total += detalle.precio * detalle.cantidad 
        self.detalleVenta.append(detalle)

    def mostrarVenta(self,empNombre,empRuc):
        print("Empresa: {:17} Ruc: {}".format(empNombre,empRuc))
        print("Factura #: {:13} Fecha: {}".format(self.factura,self.fecha))
        self.cliente.mostrarCliente() # solo muestra el dato por momento
        print("Linea Articulo      Precio  Cantidad  Subtotal")
        for det in self.detalleVenta:
          print("{:5} {:15} {} {:6} {:10}".format(det.linea,det.articulo.descripcion,det.precio,det.cantidad,det.precio * det.cantidad )) 
        print("Total Venta: {:30}".format(self.total))  

# cli1 = Cliente("Viki","0955189756","0960392786")
 
# empres = Empresa()
# cli1 = ClientePersonal("Viki","0955189756","1324657829", False)
# print(cli1.getCedula())
# arti1 = Art??culo( "Az??car",2.50, 200) 
# arti2 = Art??culo( "Leche",1.50, 100)  
# today = date.today()
# fecha = date(2021,8,15) 
# venta = CabVenta("F001", date.today(),cli1)
# venta.AgregarDetalle(arti1,4)
# venta.AgregarDetalle(arti2,6)
# venta.mostrarVenta(empres.nombre,empres.ruc)
# empres.mostrarEmpresa()
# print(empres.nombre)  

# cli = ClienteCoorporativo("Viki","0955189756","1324657829","#0002")
# cli.mostrarCliente() 
# print(cli.nombre)
# cli.contrato = "#003"
# print(cli.contrato)  

# cli = ClientePersonal("Viki","0955189756","1324657829", True)
# cli.mostrarCliente()  

# arti1 = Art??culo( "Az??car",2.50, 200) 
# arti1.mostrarArticulo()
# print(Art??culo.iva)

# arti2 = Art??culo( "Leche",1.50, 100) 
# arti2.mostrarArticulo()  
# print(Art??culo.iva)

# arti3 = Art??culo( "Pan",0.30, 150) 
# arti3.mostrarArticulo()  

# print(Art??culo.iva) 

class InterfaceSistemaPago (ABC):
    @abstractmethod
    def pago(self): 
        pass

    @abstractmethod
    def saldo(self):  
        pass

class PagoTarjetaImplements(InterfaceSistemaPago):
    def pago(self):
        return "Pago tarjeta" 
    
    def saldo(self):
        return "Saldo Tarjetarebajo" 

class PagoContratoImplements(InterfaceSistemaPago):
    def pago(self):
        return "Pago Contrato" 
    
    def saldo(self):
        return "Saldo Contrato rebajo"

class Vendedor():
    def __init__(self,nombre):
        self.nombre = nombre
    
    def moduloPagp(self,contratoV):
        return contratoV.pago()
    

pagoTarjeta = PagoTarjetaImplements()
print(pagoTarjeta.pago()) 
Contrato = PagoContratoImplements()
#print(Contrato.pago())
ven1 = Vendedor("Viki")
print(ven1.moduloPagp(Contrato)) 