'''
Ejercicio 1. Nos piden que escribamos una función que le pida al usuario que ingrese un
número positivo. Si el usuario ingresa cualquier cosa que no sea lo pedido se le debe informar
de su error mediante un mensaje y volverle a pedir el número.
'''


            
def _numeropositivo2(n):
    if n > 0:
        return True
    else:
        return False
    # return n > 0

def numeropositivo2():
    n = int(input("Ingrese un numero positivo: "))
    while not _numeropositivo2(n):
        print("\nEl numero ingresado es negativo")
        n = int(input("\nIngrese un numero positivo: "))
numeropositivo2()

def test_numeropositivo2():
    assert _numeropostivo2(2) == True
    assert _numeropostivo2(8) == True
    assert _numeropostivo2(123) == True
    assert _numeropostivo2(5465684523) == True
    assert _numeropostivo2(-2) == False
    assert _numeropostivo2(-123123412) == False
    
    
