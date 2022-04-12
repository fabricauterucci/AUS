'''
3) Escriba un programa que cuente cúantas veces aparecen cada una de las vocales en
una cadena. No importa si la vocal aparece en mayúscula o en minúscula.
'''

def ej3():
    cadena = input("Ingrese la palabra para saber cuantas vocales tiene")
    print(main(cadena))


def main(cadena): 
    count1 = count2 = count3 = count4 = count5 = 0

        
    for x in cadena:
        if x == 'a':
            count1 += 1
        elif x == 'e':
            count2 += 1
        elif x == 'i':
            count3 += 1
        elif x == 'o':
            count4 += 1
        elif x == 'u':
            count5 += 1
    return(count1,count2,count3,count4,count5)
