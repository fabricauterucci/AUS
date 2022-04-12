'''
Ejercicio 4. Escriba una función que reciba dos números como parámetros, y devuelva cuán-
tos múltiplos del primero hay, que sean menores que el segundo.
a) Implementarla utilizando un ciclo for, desde el primer número hasta el segundo.
b) Implementarla utilizando un ciclo while, que multiplique el primer número hasta que sea
mayor que el segundo.
c) Comparar ambas implementaciones: ¿Cuál es más clara? ¿Cuál realiza menos operacio-
nes?
'''


def ejercicio4a():
    x = int(input("Ingrese el primer parametro"))
    y = int(input("Ingrese el segundo parametro"))
    count = 0

    for i in range (x,y+1):
        if i%x == 0:
            count += 1
    if count == 1:  
        print("Hay",count,"multiplo")
    elif count > 1 :
        print("Hay",count,"multiplos")
    else:
        print("No hay multplos")
    return count


    

def ejercicio4():
    x = int(input("Ingrese el primer parametro"))
    y = int(input("Ingrese el segundo parametro"))
    count = 0

    while y<=x:
        x = x/y
        count+= 1

    if count == 1:  
        print("Hay",count,"multiplo")
    elif count > 1 :
        print("Hay",count,"multiplos")
    else:
        print("No hay multplos")
            

