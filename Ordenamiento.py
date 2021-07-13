class Ordenar: 
    def __init__(self, lista):
        self.lista = lista
    def borbuja(self): 
        for l in range(len(self.lista)):
            for m in range(l + 1, len(self.lista)):
                if self.lista[l] > self.lista[m]:
                    auxi = self.lista[l]
                    self.lista[l] = self.lista[m]
                    self.lista[m] = auxi  
    def insertar (self, valor):
        self.borbuja()
        auxilista = []
        enc = False
        for posi , elem in enumerate (self.lista):
            if elem > valor:
                auxilista.append (valor) 
                enc = True
                break
        if enc : self.lista = self.lista[0:posi] + auxilista + self.lista[posi:]
        else: self.lista.append(valor)
        return self.lista

    def insertar2 (self, valor):
        self.borbuja()
        auxilista = []
        enc = False
        for posi , elem in enumerate (self.lista):
            if elem > valor:
                enc = True
                break
        if enc : 
            for l in range(posi):
                auxilista.append(self.lista[l])
            auxilista.append(valor) 
            for m in range (posi, len(self.lista)):
                auxilista.append(self.lista[m])
            self.lista = auxilista
        else:
            self.lista.append(valor)
        return self.lista
orde1 = Ordenar([3,35,18,30,27])
print(orde1.insertar(9)) 
orde2 = Ordenar([10,100,1000,10000,1000000])
print(orde2.insertar2(1))
# orde1.borbuja()
# print(ord)