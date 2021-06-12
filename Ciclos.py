class Ciclo:
    def __init__(self, num1 = 34):
        self.numer = num1
    
    def usoWhile (self):
        # ciclo repetitivo que se ejecuta mediante verdadero y su salida es por falso
        elemento = input("Ingrese una vocal:")
        elemento = elemento.lower()
        while elemento not in ("a","e","i","o","u"):
            elemento = input("Ingrese una vocal:").lower()
        print("!Excelente¡ el elemento : {} es una vocal".format(elemento))
ciclo1 = Ciclo()
ciclo1.usoWhile()