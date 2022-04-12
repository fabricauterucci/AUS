'''
2) Escriba una función llamada elimina que tome una lista y elimine el primer y último
elemento de la lista y cree una nueva lista con los elementos que no fueron eliminados.
'''

def elimina(lista =[]):
    nuevalista = []
    for x in lista:
        if x != lista[0] and x!= lista[len(lista)-1] :
            nuevalista += [x]

    print(nuevalista)

def elimina2(lista = []):
    print(lista[1:len(lista)-1])
