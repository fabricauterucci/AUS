def ejercicio13():
    m =int(input("ingrese la cantidad de montos: "))
    lista_montos = []
    for i in range (0,m):
        monto = int(input("Ingrese los montos"))
        lista_montos = lista_montos + [monto]
    print("La suma total de montos es",suma_dinero(lista_montos))

def suma_dinero(lista_montos):
    #lista_montos = [1000,2000]
    total = 0
    for monto in lista_montos:
        total = total + monto
    return total
