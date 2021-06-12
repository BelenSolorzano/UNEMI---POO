#FUNCIONES EN PYTHON - DEF
'''Función con retorno de valor'''
def promedio(nota):
    sum = 0
    for l in nota :
        sum += l
    return sum /len(nota)
#llamada a función
listnotas = [9,10,8,8,9]
pro = promedio(listnotas)
print("Sus notas son:{} y su promedio total es : = {} /10 ".format(listnotas,pro))