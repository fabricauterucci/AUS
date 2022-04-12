def cuad(n):
    return n*n

def suma_cuadrados(n):
    suma = 0
    for x in range (1, n+1):
        suma = suma + cuad(x)
    return suma

print( 'La suma de los primeros 100 cuadrados es',suma_cuadrados(100) )

