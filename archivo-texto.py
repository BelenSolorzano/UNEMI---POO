def leer():
    with open("invitados.txt", "r", encoding="UTF-8") as f:
        invitado = [linea[:-1] for linea in f]
        print(invitado)
        
def escribir():
    invitados1=  ["Lupe", "Leo", "Jasmin", "Alberto", "Gloria"]
    invitados2= ["Viqui", "Dominik", "Mikey", "Lisa", "Stefanie"]

    with open("invitados.txt", "w", encoding="UTF-8") as f:
        for nombre in invitados2:
            f.write(nombre)
            f.write("\n")

def run():
    escribir()
    leer()

if __name__ =="__main__":
    run()