def ej1(n = 100):
    h = ' '
    while n>=20 :
        h += ' '+ str(n)
        n -= 5
    return h


'''Explicacion:
El programa tiene de argumento un numero,
mientras el numero sea mayor o igual que 20, el programa
devuelve una variable que almacena numeros desde n hasta
que el numero sea menor que 20, el numero menos cinco
'''

def ej2(a,b,c):
    n = 2
    suma = 0
    sumas = 0

    if a/b >30:
        suma = a/c*b**3
        return suma
    if a/b <= 30 :
        while n <= 30:
            sumas += n**2
            n +=2
        return sumas
