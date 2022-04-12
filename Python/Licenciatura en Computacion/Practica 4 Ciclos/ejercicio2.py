'''
Ejercicio 2. Escriba un programa que permita al usuario ingresar un conjunto de notas, pre-
guntando a cada paso si desea ingresar más notas, e imprimiendo el promedio correspondiente,
al finalizar la toma de datos
'''
def _ejercicio2():
    m = int(input("Ingrese la cantidad de notas"))
    lista_notas = []
    for i in range (0,m):
        nota = int(input("Ingrese las notas"))
        lista_notas = lista_notas + [nota]
    print(promedio_notas(lista_notas))

def promedio_notas(lista_notas):
    total = 0
#    lista_notas = [1,2,4,2]
    for nota in lista_notas:
        total = total + nota
    return total / len(lista_notas)
        
        


    
    
''''
def ejercicio2():
    n = int(input("Ingrese una nota.\n"))
    x = 0
    contador=0
    resp =0
    prom = 0
    
        
    while(n<=10 and n>=0):
        lista
        _ejericio2(n)
        resp = int(input("Desea ingresar otra nota?\n"
              "1)Si\n"
              "2)No\n"))
        if resp == 1:
            n = int(input("Ingrese una nota\n"))

        elif resp == 2:
            print("Promedio es:\n",x/contador)
            break
_ejercicio2()
'''
def test_promedio_notas():
    assert promedio_notas([1,10,4]) == 5

        
