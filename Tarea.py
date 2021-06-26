class Deber:
    def __init__(self):
        pass 
    def pJornadaExtra (self):
        h_trabajadas, h_extra, h_extra_triple = 0, 0, 0
        v_hora, p_hora_extras, p_total = 0, 0, 0 
        h_trabajadas = int(input("Ingrese horas que trabajó: "))
        v_hora = float(input("Ingrese valor de pago por hora: $ "))
        if (h_trabajadas > 40):
            h_extra = h_trabajadas - 40
            if (h_extra > 8):
                h_extra_triple = h_extra - 8 
                p_hora_extras = v_hora * 2 * 8 + v_hora * 3 * h_extra_triple
            else: 
                p_hora_extras = v_hora * 2 * h_extra
            p_total = v_hora * 40 + p_hora_extras
        else:
            p_total = v_hora * h_trabajadas
        print("Horas trabajadas: $ {} | Horas extras: $ {} | Horas triples: $ {} " 
        "| Pago en velor extra: $ {} | Pago total del empleado: $ {}".format(h_trabajadas,
        h_extra, h_extra_triple, v_hora, p_hora_extras, p_total)) 
        print("_____________________________________________________________________________________________________")
        
    def mayor (self):
        nu1,nu2,nu3 = 0,0,0
        nu1 = int(input("Ingrese primer número: ")) 
        nu2 = int(input("Ingrese segundo número: "))
        nu3 = int(input("Ingrese tercer número: ")) 
        if (nu1 > nu2 > nu3): 
            print("El número mayor entre los tres es : {}".format(nu1))
        elif (nu2 > nu1 > nu3):              
            print("El número mayor entre los tres es : {}".format(nu2))
        else:
            print("El número mayor entre los tres es : {}".format(nu3))

even = Deber()
even.pJornadaExtra()
even.mayor()


