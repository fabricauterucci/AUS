'''
Ejercicio 8. Escribir dos funciones que resuelvan los siguientes problemas:
a) Dado un número entero n, indicar si es par o no.
b) Dado un número entero n, indicar si es primo o no.
'''
print("Ingrese ej8a() para el A y ej8b() para el B") 
def ej8a():
    n = int(input("Ingrese un numero entero: "))

    if n%2 == 0:
        print("\nEl número es par")

    else:
        print("El número es impar")
        

def ej8b():
    while(1):
        n = int(input("\nIngrese un numero entero: "))
        c = 0

        for i in range(2,n):
            if n%i == 0:
                c= c+1

        if c >1:
            print("\nEl numero no es primo")

        else:
            print("\nEl número es primo")
