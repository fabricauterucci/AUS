'''
Ejercicio 9. Defina una función buscar que toma una lista de palabras listaPalabras
como parámetro y:
a) solicita que se ingrese una palabra palabraABuscar
b) se verifica si palabraABuscar ingresada se encuentra presente en listaPalabras
c) se muestra un cartel indicando si está o no la palabra buscada
'''

def buscar(listaPalabras =[]):
    contador = 0
    palabraABuscar = input("Ingrese una palabra para buscarla en la lista")
    for x in listaPalabras:
        if x == palabraABuscar :
            contador+= 1            
    if contador == 0:
        print("La palabra no esta en la lista")
    elif contador == 1:
        print("La palabra '",palabraABuscar,"'esta en la lista")
    else:
        print("La palabra '",palabraABuscar,"' aparece", contador, "veces en la lista.")
    
