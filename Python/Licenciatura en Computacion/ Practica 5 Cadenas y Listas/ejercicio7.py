'''
Escriba una función ordenada que tome una lista como parámetro y devuelva True si la
lista está ordenada en orden ascendente y devuelva False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna F alse
'''

def ordenada(lista = []):
    for x in lista[:len(lista)-1]:
        for y in lista[1:len(lista)]:
             j = x<=y
   
    print(j)
