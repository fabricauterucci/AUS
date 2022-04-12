'''
Ejercicio 13. Se pide construir un programa, el cual dada una lista que representa montos de
dinero ingresados por el usuario, devuelva como resultado la suma de los montos presentes
en la lista. Para esto último se pide definir una función suma_dinero que toma como entrada
la lista con los montos de dinero y calcula dicha suma.

Ejercicio 14. Modifique el programa anterior de forma tal que:
a) Permite ingresar los valores sin corroborar en el momento si corresponden a montos de
dinero o no ( si son o no positivos)
b) Cree una función montos_positivos la cual devuelve True si todos los valores de la
lista son positivos, y False en caso contrario.
c) Cree una función checked_suma la cual recibe como entrada una lista de números, y
devuelve la suma de todos sus elementos si la lista se corresponde con una lista de
montos de dinero, sino deberá devolver un error.



1)Analisis del problema:
En un principio el programa pide ingresar montos de dinero , sin importar si son positivos o negativos.
Luego el programa, asume una nueva funcion que corrobora que el monto sea positivo.
Por ultimo , el programa suma todos los montos si son positivos, en caso contrario emite un mensaje de error.

2)Especificacion del problema:
Datos de entrada: son los montos que el usuario desea ingresar, para almacenarlos en una lista, y luego sumarlos
Datos de salida: devuelve los montos sumados, o un mensaje de error si estos son negativos, o cadena.

3)Diseño:
a)Como entrada el usuario ingresa los montos, el programa suma todos, y devuelve la sumatoria del total de ellos.
b)El programa distingue de los montos positivos, y los negativos.
c)Si la lista es de montos positivos, esta los calcula. En caso contrario el programa imprime Error.




4)Implementacion:

'''
def ejercicio14(m):
    
    lista_montos = []
    for i in range (0,m):
        monto = float(input("Ingrese los montos"))
        lista_montos = lista_montos + [monto]
    print("La suma total de montos es",suma_dinero(lista_montos))

def suma_dinero(lista_montos):
    #lista_montos = [1000,2000]
    total = 0
    for monto in lista_montos:
        total = total + monto
    return total

def montos_positivos(lista_montos):
    count = 0
    for i in range (0,len(lista_montos)):
        if lista_montos[i] > 0:
            count += 1
    if count == len(lista_montos):
        return True
    else :
        return False


def checked_suma(lista_montos): #Aclaraciòn: en caso de ingresar una cadena,devuelve error por comparar un str con un int.
    sumatoria = 0
    

    if montos_positivos(lista_montos) == True :
        for i in range (0,len(lista_montos)):
            sumatoria = sumatoria + lista_montos[i]
        return sumatoria
        
    else:
        return "Error" #Devuelve Error, en caso de ingresar un numero negativo
        
        


'''
5)Prueba:
'''

def test_suma_dinero():
    assert  suma_dinero([1000,2000,3000]) == 6000
    assert suma_dinero([1000,-1000]) == 0


def test_montos_positivos():
    assert montos_positivos([5000,-500]) == False
    assert montos_positivos([5000, 500]) == True

def test_checked_suma():
    assert checked_suma([-500,1000]) == "Error"
    assert checked_suma([100,1000]) == 1100
        

