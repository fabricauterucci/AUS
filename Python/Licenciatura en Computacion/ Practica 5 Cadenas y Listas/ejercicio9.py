'''

5) Escriba una función llamada eliminaDuplicados que tome una lista y devuelva una
nueva lista con los elementos únicos de la lista original. No tienen porque estar en el
mismo orden.

'''
def duplicado(lista = []):
    listaa = []
    for i in lista:
        if i not in listaa:
            listaa += [i]
    return(listaa)
    
def impri():
    lista = []
    n = int(input("Ingrese la cantidad de elementos de la lista"))
    for x in range(n):
        numero = int(input("Ingrese un numero de la lista"))
        lista += [numero]
            
   # print(list(set(lista)))
    print(duplicado(lista))
