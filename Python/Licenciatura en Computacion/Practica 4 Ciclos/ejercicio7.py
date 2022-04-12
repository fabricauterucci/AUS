'''
Ejercicio 7. Potencias de dos
a) Escribir una función es_potencia_de_dos que reciba como parámetro un número natural, y devuelva True si el número es una potencia de 2, y False en caso contrario.

b) Escribir una función que, dados dos números naturales pasados como parámetros, devuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
(0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos,
descripta en el punto anterior.
'''

def es_potencia_de_dos(numero):
    if numero < 1:
        return False
    if numero <= 2:
        return True
    i = 2
    while True:
        i *= 2
        if i == numero:
            return True
        if i > numero:
            return False

def suma_potencias(n1,n2):
    i = 0
    for x in range(n1,n2+1):
        if es_potencia_de_dos(x) == True:
            i = i+x
        
    print(i)
        
        

def parametros():
    n1 = int(input("Ingrese el primer parametro del intervalo"))
    n2 = int(input("Ingrese el segundo parametro del intervalo"))

    suma_potencias(n1,n2)
    
        
