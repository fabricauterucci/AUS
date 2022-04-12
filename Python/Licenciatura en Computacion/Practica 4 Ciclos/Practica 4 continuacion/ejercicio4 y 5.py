def ej4(n = 1):
    p = 0
    i = 0
    while n <= 100:
        if n%2 == 0:
            p += n
            print(p)
        else:
            i += n
            print(i)            
        n += 1

    return 'Pares = ' + str(p) + 'e Impares: '+str(i)

'''
La funcion toma un numero n como argumento e imprime por pantalla la suma de los numeros pares
por un lado e impares por otro lado desde n hasta 100.
'''

def ej5(s=5):
    for x in s:
        for z in x:
            print(z)
        print('***************')
'''
no funciona
'''
