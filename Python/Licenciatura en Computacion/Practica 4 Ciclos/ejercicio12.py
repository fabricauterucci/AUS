'''
Ejercicio 12. Defina una función cuentaAparicionesCadena que toma un string palabra
como parámetro y:
a) solicita que se ingrese un caracter caracterABuscar
b) se cuenta la cantidad de veces que caracterABuscar esté presente en palabra
c) se muestra un cartel indicando la cantidad de veces que esta presente o, si no se en-
cuentra
d) Compare este problema con el anterior. Analice qué tuvo que cambiar entre uno y otro.
'''

print('Ingrese funcion("palabra") para ejecutar el programa')
def cuentaAparicionesCadena(palabra):
    caracterABuscar = input("Ingrese el caracter a buscar: ")
    count = 0
    
    for x in list(palabra):
        if caracterABuscar == x:
            count+= 1

    if count == 0 :
        print("La letra",caracterABuscar,"no se encuentra en la palabra.")
    if count == 1 :
        print("La letra",caracterABuscar,"se encuentra",count,"vez en la palabra.")
    if count > 1:
        print("La letra",caracterABuscar,"se encuentra",count,"veces en la palabra.")

