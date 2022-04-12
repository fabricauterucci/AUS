'''

EJERCICIO XI:
Construya un programa el cual sobre una lista de números ingresados por el
usuario, y un número n también dado, calcule la cantidad de elementos de la lista ingresada
que son mayores a n. Utilizar funciones por separado para el ingreso de los datos en el arreglo
y el cómputo de elementos mayor que el dado dado.

'''

'''
def lista():
    m = int(input("Ingrese la cantidad de elementos de la lista"))
    lista = []
    count = 0
    for x in range(m):
        numero = int(input("Ingrese otro numero para la lista"))
        lista += str(numero)
        
    n = int(input("Ingrese un numero para saber que elementos de la lista son mayores"))

'''

def datos():
    lista = []
    m = int(input("Ingrese la cantidad de elementos de la lista"))
    for x in range(m):
        numero = int(input("Ingrese otro numero para la lista"))
        lista += str(numero)

    n = int(input("Ingrese un numero para saber que elementos de la lista son mayores"))

    ejercicio11(lista,n)
    


            
        
def ejercicio11(lista,n):
    count = 0
    for x in lista:
        if n < int(x):
            count+= 1


    print("Hay",count," elementos de la lista, mayores que",n)
    
