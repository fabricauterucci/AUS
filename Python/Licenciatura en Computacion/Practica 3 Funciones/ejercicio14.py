'''Escribir una función que, dados cuatro números, devuelva el mayor producto
de dos de ellos. Por ejemplo, si recibe los números 1, 5, (−2), (−4) debe devolver 8, que es el
producto más grande que se puede obtener entre ellos (8 = (−2) × (−4)).
'''

def cuatroprod():
    print("El programa calcula el mayor producto entre cuatro valores.\n")
    a = int(input("Ingrese un numero: \n"))
    b = int(input("Ingrese otro numero: \n"))
    c = int(input("Ingrese otro numero: \n"))
    d = int(input("Ingrese otro numero: \n"))

    x = a*b
    y = a*c
    z = a*d
    x1 = b*c
    x2 = b*d
    x3 = c*d
    
    

    print("El maximo producto es", max(x,y,z,x1,x2,x3))

cuatroprod()
