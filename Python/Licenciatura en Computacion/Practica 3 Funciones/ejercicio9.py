'''
Ejercicio 9.

Escribir una implementación propia de la función abs, que devuelva el valor
absoluto de cualquier valor que reciba.
'''

def abs():
    n = int(input("Ingrese el numero para saber su absoluto: "))

    if n < 0:
        print("El numero absoluto es",-n)

    if n >= 0:
        print("El numero absoluto es",n)

abs()
    
