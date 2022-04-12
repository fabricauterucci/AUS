
def volcubo(arista):
    print("El volumen del cubo es ",arista**3)

def areacubo(arista):
    print("El area del cubo es",6*(arista**2))

'''
Defina una función que según el valor que ingrese el usario, se calcule el volumen, o
el área de un cubo. Tener en consideración un valor por defecto, si el valor ingresado
no fuera el adecuado, en dicho caso deberá calcular el área de un cubo. Reutilizar las
funciones de los items anteriores.
'''

def ejercicio16c():
    arista = int(input("Ingrese la arista del cubo: "))
    n = int(input("Ingrese 1 para saber el volumen del cubo, o 2 para saber el area del cubo: "))

    if n == 1 :
        volcubo(arista)
    else :
        areacubo(arista)



'''
Modifique la función definida en item anterior para que, en caso de no recibir un valor
apropiado nos muestre el siguiente mensaje en pantalla "Valor no soportada por la fun-
ción.".
'''

def ejercicio16d():
    arista = int(input("Ingrese la arista del cubo: "))
    n = int(input("Ingrese 1 para saber el volumen del cubo, o 2 para saber el area del cubo: "))

    if n == 1 :
        volcubo(arista)
    elif n ==2 :
        areacubo(arista)
    else :
        print("Valor no soportada por la función")

            
ejercicio16d()
