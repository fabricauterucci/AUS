def factorial():
    print("Imprime el factorial de un numero")
    n1=int(input("Ingrese el numero: "))

    fact = 1
    for x in range (1,n1+1):
        fact= fact * x
    print("el factorial de",n1,"es de ",fact)
