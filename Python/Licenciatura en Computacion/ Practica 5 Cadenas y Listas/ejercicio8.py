'''
4) Escriba una función llamada duplicado que tome una lista y devuelva True si tiene algún
elemento duplicado. La función no debe modificar la lista.
'''

def duplicado(lista = []):
    count = 0
    
    for x in lista:
        for y in lista:
            
            if x == y :
                count += 1
            if count > len(lista):
                return True
    return False
                
                
    

def impri():
    lista = []
    n = int(input("Ingrese la cantidad de elementos de la lista"))
    for x in range(n):
        numero = int(input("Ingrese un numero de la lista"))
        lista += [numero]
            
    print(duplicado(lista))



        
impri()                    
            





