# -*- encoding: utf-8 -*-
'''
Ejercicio 5. Manejo de contraseñas
a) Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
c) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó
o no la contraseña correctamente, mediante un valor booleano (True o False).

'''


'''Analisis del problema:
a)Se desea ingresar una contraseña, hasta que sea la contraseña correcta.
b)Se desea ingresar una contraseña, con un limite fijado.
c)Se desea ingresar una contraseña, que devuelve True si es correcta , y False si no lo es.

Especificacion del problema:
a)Los datos de entrada se van a comparar con la contraseña ya almacenada en la función, si esta es valida,
el programa continuará. En caso contrario pedirá la contraseña hasta que sea la correcta.
b) Lo mismo que el item anterior, con la diferencia de que no tenemos intentos ilimitados para introducir la contraseña

Diseño :
El programa pide al usuario una contraseña, la compara con la contraseña almacenada, y este devuelve si es correcta o no.


Implementación:
'''
def ej5a(contraseña):
    """
    Pequeño resumen del funcionamiento de la función 'ej5a'.
    Args: argumento1: la funcion toma como argumento la contraseña inventada    
    Returns: no tiene
    """
    

    contraseñax = input("Ingrese la contraseña: ")

    while str(contraseña) != contraseñax :
        contraseñax = input("Contraseña incorrecta. Ayuda: tiene cuatro digitos. Ingrese la contraseña: ")      

    else:
        print("Contraseña correcta")


def ej5b(contraseña):
    """
    Pequeño resumen del funcionamiento de la función 'ej5b'.
    Args: argumento1: la funcion toma como argumento la contraseña inventada    
    Returns: no tiene
    """

    contraseñax = input("Ingrese la contraseña, tiene 5 intentos: ")
    intentos = 4
    while str(contraseña) != contraseñax and intentos > 0 :
        contraseñax = input("Contraseña incorrecta. Ingrese la contraseña: ")
        intentos-= 1
        print("Tiene",intentos,"intentos")

        if intentos == 0 :
            print("Contraseña incorrecta")
            break

    else:
        print("Contraseña correcta")

def ej5c(contraseña):
    """
    Pequeño resumen del funcionamiento de la función 'ej5c'.
    Args: argumento1: la funcion toma como argumento la contraseña inventada    
    Returns: devuelve "True" si la contraseña es correcta, y "False" en caso contrario.
    """

    contraseñax = input("Ingrese la contraseña, tiene 5 intentos: ")
    intentos = 4
    while str(contraseña) != contraseñax:
        if intentos > 0 :
            contraseñax = input("Contraseña incorrecta. Ingrese la contraseña: ")
            intentos-= 1
            print("Tiene",intentos,"intentos")

        if intentos == 0 :
            return False
            break

    else:
        return True

'''
Prueba: como el programa tiene input no es posible utilizar pytest, pero se puede correr con el interprete
y verificar:

ej5c(1515)
Ingrese la contraseña, tiene 5 intentos: 1
Contraseña incorrecta. Ingrese la contraseña: 2
Tiene 3 intentos
Contraseña incorrecta. Ingrese la contraseña: 3
Tiene 2 intentos
Contraseña incorrecta. Ingrese la contraseña: 4
Tiene 1 intentos
Contraseña incorrecta. Ingrese la contraseña: 5
Tiene 0 intentos
False

ej5c(1515)
Ingrese la contraseña, tiene 5 intentos: 1515
True


'''

