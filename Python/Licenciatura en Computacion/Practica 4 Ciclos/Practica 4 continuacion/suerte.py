from random import *

def dado():
    n = randint(1,7)
    count = 0
    while n != 7:
        n = randint(1,7)
        count += 1
        print(n)

    print("El dado se lanzó",count,"veces")
        

