from random import *


'''
1) Cartas como tuplas
a) Proponga una representación con tuplas para las cartas de la baraja francesa.
b) Escriba una función poker que reciba cinco cartas de la baraja francesa e informe
(devuelva el valor lógico correspondiente) si esas cartas forman o no un poker (es
decir que hay 4 cartas con el mismo número).
'''

def cartas():
    treboles = ("♣","♣♣","♣♣♣","♣♣♣♣","♣♣♣♣♣","♣♣♣♣♣♣","♣♣♣♣♣♣♣","♣♣♣♣♣♣♣","♣♣♣♣♣♣♣♣♣♣","J♣","Q♣","K♣","A♣")
    corazones = ("❤","❤❤","❤❤❤","❤❤❤❤","❤❤❤❤❤","❤❤❤❤❤❤","❤❤❤❤❤❤❤","❤❤❤❤❤❤❤❤","❤❤❤❤❤❤❤❤❤","J❤","Q❤","K❤","A❤")
    picas = ("♠","♠♠","♠♠♠","♠♠♠♠","♠♠♠♠♠","♠♠♠♠♠♠","♠♠♠♠♠♠♠","♠♠♠♠♠♠♠","♠♠♠♠♠♠♠♠","♠♠♠♠♠♠♠♠♠","J♠","Q♠","K♠","A♠")
    diamantes =  ("♦","♦♦","♦♦♦","♦♦♦♦","♦♦♦♦♦","♦♦♦♦♦♦","♦♦♦♦♦♦♦","♦♦♦♦♦♦♦♦","♦♦♦♦♦♦♦♦♦","J♦","Q♦","K♦","A♦")

    baraja = treboles + corazones + picas + diamantes
    #print(baraja) 

    mano = ()

    for x in range (5):
        mano += baraja[randint(0,52)],

    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    
    for x in treboles:
        for y in mano:
            if x == y:
                count += 1

    for x in corazones:
        for y in mano:
            if x == y:
                count1 += 1

    for x in picas:
        for y in mano:
            if x == y:
                count2 += 1

    for x in diamantes:
        for y in mano:
            if x == y:
                count3 += 1
            

    if count >= 4 or count1 >= 4 or count2 >= 4 or count3 >= 4:
        print("POKER ! la mano es ",mano)
    else:
        print("No hay poker, la mano es ",mano)

                

                
