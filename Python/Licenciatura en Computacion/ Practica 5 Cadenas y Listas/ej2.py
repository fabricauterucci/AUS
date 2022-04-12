'''
Escriba un programa que contenga a la función contar(l, x) que cuente cuántas ve-
ces aparece un carácter l dado en una cadena x.
'''

def contar():
    CaracterABuscar = input("Ingrese el caracter a buscar")
    cadena = input("Ingrese la cadena")

    print(funcion(CaracterABuscar,cadena))



def funcion(CaracterABuscar,cadena):
    count = 0

    for x in list(cadena):
        if CaracterABuscar == x:
            count += 1
    
    return(count)

def test_funcion(CaracterABuscar,cadena):
    assert funcion(h,hola) == 1
