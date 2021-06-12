class Valor: 
    contador = 0 #variable de clase (opcional)
    #__init__ Método constructor que se ejecuta al momento de instanciar la clase que tiene como 
    #objetivo crear e inicializar los atributos d ela clase. 
    # Self es un objeto que representa a la clase que se crea.
    def __init__(self,n1 = 0, n2 = 3):
        self.valor1 = n1  # variable de instancia
        self.valor2 = n2
        #valor = n1 + n2
        self.valor3 = n1
        #variables de instancias

    def comparación(self):
        # if / elif / else : condicionan la ejecución de uno o varios bloques
        # de sentencias al momento dde cumplir con una o varias condiciones.
        if self.valor1 == self.valor2:
            print("valor1:{}, valor2:{}: son iguales".format(self.valor1,self.valor2))
        elif self.valor1 == self.valor3:
             print("valor1:{}, valor3:{}: son iguales".format(self.valor1,self.valor3))
        else:
            print("Los valores no son iguales")
# usar clase
# condición1 = Valor ()
# print(condición1.valor1)
# print(condición1.valor2)

condición2 = Valor(30,12)
condición2.comparación() # llama a un metodo de la clase
print(condición2.valor1) # llamada a un atributo de la clase
        
