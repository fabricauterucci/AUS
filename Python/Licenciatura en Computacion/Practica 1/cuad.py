def cuadrados():
    print("Se calcularan los cuadrados entre dos numeros ingresados: \n")
    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))

    for x in range (n1,n2+1):
        print('el cuadrado de',x,' es',x*x)


cuadrados()
