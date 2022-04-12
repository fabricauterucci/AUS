def imprimir_cuad():
    print('Se calculará el cuadrado del intervalo de dos numeros ingresados')

    n1 = int (input ('Ingrese un numero entero: '))
    n2 = int (input ('Ingrese otro numero entero: '))
   

    for x in range(n1, n2+1): #ver
        
        print('El cuadrado de',x,'es', x*x)
        
        


imprimir_cuad()
