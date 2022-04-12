'''
Ejercicio 8. Vamos a escribir un programa que permita crear una lista de palabras, para esto
el programa tiene que:

a) pedir un número numeroPalabras que va a representar la cantidad de palabras que va
a tener la lista

b) solicitar que se ingresen las numeroPalabras que se ingresó en el punto anterior. Para
esto, recuerde que vimos el operador + para agregar elementos a una lista.

c) luego de que se ingresen todas las palabras se debe mostrar la lista de palabras obtenida

'''

def ejercicio8():
    listapalabras = []
    numeroPalabras = int(input("Ingrese la cantidad de palabras que va a tener la lista"))
    while numeroPalabras < 0:
        numeroPalabras = int(input("Ingrese una cantidad de palabras positivas"))
    else:        
        for x in range(0, numeroPalabras):
            palabra = input("Ingrese una palabra")
            listapalabras += [palabra]
    print(listapalabras)


def ej8re(lista=[],n = 5):
    if n == 0:
        return lista
    for i in range(0,n):
        palabra= input("Ingrese una palabra")
        lista += [palabra]

    print(lista)

    
        
