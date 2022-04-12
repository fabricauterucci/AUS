from random import *
'''
3) Simule n lanzamientos de un juego con un dado con las siguientes reglas: Si sale 6 gana
4 dolares; con un 3 gana 1 dólar; si sale 1 sigue jugando y, con 2,4 o 5 pierde 2 dolares.
Muestre los valores que salen y, el resultado final del juego.
'''

def dolares():
    n = int(input("Ingrese la cantidad de lanzamientos"))

    dolares = 0
    count = 0
    
    while count != n :
        x = randint(1,7)

        if x == 6:
            print("Felicitaciones! ganaste 4 dolares :D! ")
            dolares += 4
        elif x == 3:
            print("Peor es nada! Ganaste un dólar")
            dolares += 1
        while x == 1:
            x = randint(1,7)
            print("Ganaste un tiro gratis ")
        if x == 2 or x == 4 or x == 5:
            print("Perdiste dos dolares :( ")
            dolares += -2
        count += 1

    print("El total de dolares acumulados es U$D",dolares)
        
