#FUNCIONES EN PYTHON - DEF
'''Funciones sin retorno'''
def vocales(frase):
    for voc in frase:
        if voc in('a','e','i','o','u'):
            print(voc)
'''Llama a finción'''
palabra = input('Ingrese palabra:')
vocales(palabra.lower())
