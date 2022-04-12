'''
1) Escriba un programa que tenga una función que tome una cadena y muestre cada caracter
que la forma del último al inicial.
'''

def cadena1(n):
    ret = []
    for i in range(len(n),0,-1):
        ret += [n[i-1]]
    return ret

def ejercicio1():
    n = input("Ingrese una palabra: ")
    lista_al_reves = cadena1(n)
    for j in lista_al_reves:
        print(j)

ejercicio1()
        
