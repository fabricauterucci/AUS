'''
4) Escriba un programa que contenga la función que reciba como parámetro una cadena de
palabras separadas por espacios y devuelva, como resultado, cuántas palabras de más
de cinco letras tiene la cadena dada.
'''

def separarcadena(cadena):
    listas = []
    count = 0
    lista = []
    lista2 = []
    count1 = 0
    count2 = 0
    contadorcincoletras = 0
    
    for x in cadena:
        if x == ' ':
            count += 1
        if count == 0 :
            lista += x
            count2 += 1
       
             
        if count == 1 and x != ' ':
            lista2 += x
    listas += [lista]+ [lista2]
    print(listas)

    for x in listas:
        if len(x) >= 5:
            contadorcincoletras+= 1
    print("La cadena tiene",contadorcincoletras,"palabras con mas de cinco letras")    
    



 
 
        

        
