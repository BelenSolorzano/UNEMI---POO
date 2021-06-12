# EJEMPLO DE UNA CLASE EN PYTHON
class Fracción:
    def _init_(self,numerador,denominador):
        self.num = numerador
        self.den = denominador
    def show(self):
         print(self.num,"/",self.den)

x = Fracción(1,2)
y = Fracción(2,3)
print(x.show())
print(x.show())