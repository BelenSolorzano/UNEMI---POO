# articulo
# cliente
# venta 
# ventadet

class Artículo:
    def __init__(self,cod,des,pre,sto) :
        self.codigo = cod
        self.descripcionm = des
        self.precio = pre
        self.estock = sto
class Cliente: 
    def __init__(self,ced,nom,dir,tel) :
        self.cedula = ced
        self.nombre =  nom
        self.direccion = dir
        self.telefono = tel
class Venta: 
    def __init__(self,fac,fec,cli,tot,detalle) :
        self.factura = fac
        self.Fecha =  fec
        self.cliente = cli
        self.total = tot 
        self.detalle = detalle
class VentaDetalle: 
    def __init__(self,articulo,precio,cantidad) :
        self.articulo =  articulo
        self.precio = precio
        self.centidad = cantidad