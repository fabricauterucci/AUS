
def ej2(a,b,c):
    n = 2
    suma = 0
    sumas = 1
    if a/b > 30:
        suma = a/c*b **3
        return suma

    if a/b <= 30:
        while n <= 30:
            sumas += (n**2)
            n+=2
        return sumas



'''
-si la division entre a y b es mayor que 30, entonces devuelve
la division de a / c por b al cuadrado

-si la division entre a y b es menor o igual que treinta, entonces
el ciclo while crea un sumatoria de n al cuadrado, desde n hasta
que n sea mayor que 30, aumentando n de dos en dos.
'''


def ej3(n = 5):
    h = 0
    while n >= 20:
        h += n
        n -= 2
    return h


'''
la funcion toma valor inicial 5, pero puede ser cambiado
por el usuario, si el numero ingresado por el usuario
es menor que 20, el programa devuelve 0,si es mayor que 20
el programa devuelve el numero sumado al numero menos dos hasta que
el numero sea menor que 20.
'''

