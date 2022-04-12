'''
a) Escribir una función es_potencia_de_dos que reciba como parámetro un número na-
tural, y devuelva True si el número es una potencia de 2, y False en caso contrario.
b) Escribir una función que, dados dos números naturales pasados como parámetros, de-
vuelva la suma de todas las potencias de 2 que hay en el rango formado por esos números
(0 si no hay ninguna potencia de 2 entre los dos). Utilizar la función es_potencia_de_dos,
descripta en el punto anterior.
'''

def es_potencia(n):
    
    if n<1:
        return False
    if n>=1:
        i=1
        while i<=n:
            if i == n:
                return True
            i *= 2
            
        return False
    
        

def maina():
    n = int(input("Ingrese un número natural.\n"))
    if n>0:
        print(es_potencia(n))


def potencia(dos,n):
    
    b=0
    res=1
    while b<=n:
        res*=2
        b=+1
    return res

def suma_potencias(n1,n2):
    j=n1
    pot = 1
    while n1>=pot:
        j+=1
        pot*=2

    k=0
    pot=1
    while pot<=n2:
        k+=1
        pot*2
    if pot>n2:
        k-=1
        pot/=2

    suma=0
    dos=2
    for n in range(j,k+1):
        suma+=potencia(dos,n)
    return suma

def mainb():
    n1 = int(input("Ingrese un extremo del intervalo.\n"))   #preguntar este ejercicio
    n2 = int(input("Ingrese el otro extremo del intervalo.\n"))

    suma_potencias(n1,n2)

    if n1>0 and n2>0:
        
        print("La suma de las potencias es",suma_potencias(n1,n2))

    else:
        return



 
