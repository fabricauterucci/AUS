'''Ejercicio 10. Defina una función cuentaApariciones que toma una lista de palabras lis-
taPalabras como parámetro y:
a) solicita que se ingrese una palabra palabraABuscar
b) se cuenta la cantidad de veces que palabraABuscar esté presente en listaPala-
bras
'''

def ej10(lista=[]):
    palabrABuscar = input("Ingrese una palabra para buscar")
    count = 0
    for x in lista:
        if x == palabrABuscar:
            count += 1

    if count == 0:
        print("La palabra '",palabrABuscar,"' no se encuentra en la lista")
    else:
        print("La palabra'",palabrABuscar,"'se encuentra",count,"veces en la lista")
        
