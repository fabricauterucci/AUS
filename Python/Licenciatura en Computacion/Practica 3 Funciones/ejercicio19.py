'''
Ejercicio 19. Suponiendo que el primer día del año fue lunes, escribir una función que reciba
un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. Por
ejemplo: si recibe ’3’ debe devolver ’miércoles’, si recibe ’9’ debe devolver ’martes’.
'''

def ejercicio19():
    n = int(input("Ingrese el numero del dia que desea saber: "))
    if n>=1 and n<=366:
        if n == 1 or ((n-1)%7)==0:
            print("\nEs lunes")
        elif n == 2 or ((n-2)%7)==0:
            print("\nEs Martes")
        elif n == 3 or ((n-3)%7)==0:
            print("\nEs Miercoles")
        elif n == 4 or ((n-4)%7)==0:
            print("\nEs Jueves")
        elif n == 5 or ((n-5)%7)==0:
            print("\nEs Viernes")
        elif n == 6 or ((n-6)%7)==0:
            print("\nEs Sabado")
        elif n == 7 or ((n-7)%7)==0:
            print("\nEs Domingo")
    else:
        print("\nError")

ejercicio19()
