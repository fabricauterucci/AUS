'''
2) Simule n lanzamientos de dos dados, donde n es un valor que se debe pedir que se
ingrese por teclado. Muestre cuántas veces los dados tuvieron el mismo resultados.
'''

from random import *

def dadon():
    n = int(input("Ingrese el numero de lanzamientos"))

    x = randint(1,7)
    y = randint(1,7)
    count2 = 0
    count = 0
    while count2 != n :
        x = randint(1,7)
        y = randint(1,7)
        if x == y:
            count += 1
        print("Dado1:",x," Dado2:",y)
        count2 += 1


    print("Los dados coincidieron",count,"veces")
        
