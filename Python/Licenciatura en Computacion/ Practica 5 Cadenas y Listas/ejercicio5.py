'''
1) Escriba una función que tome una lista de números y devuelva la suma acumulada, es
decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la
suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con
el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1, 2, 3]
es [1, 3, 6].
'''

def funcion(lista = []):
    listaa = []
    sumAcumulada = 0
    for x in lista:
        sumAcumulada += x
        listaa = listaa + [sumAcumulada]
    print(listaa)
        

def ej5():
    n = int(input("Ingrese la cantidad de numeros de la lista"))

    lista = []
    
    for x in range (n):
        numero = int(input("Ingrese un numero de la lista: "))
        lista += [numero]

    funcion(lista)
