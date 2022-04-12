'''
Se pide que implemente la función busquedaDicotomica que toma una lista de pala-
bras ordenadas alfabeticamente y, una palabra a buscar y, retorna si la palabra está en
la lista o no.
'''

def busquedaDicotomica(palabra,lista=[]):
    count = 0
    count2 = 0
    for x in lista[:len(lista)//2] :
        if x == palabra :
            count += 1

    for x in lista[len(lista)//2:]:
        if x == palabra:
            count2 += 2
            
       
    if count == 1:
        print("La palabra esta antes del centro de la lista")
    elif count2 == 2:
        print("La palabra esta despues del centro de la lista")
    else:
        print("La palabra no esta dentro de la lista")
