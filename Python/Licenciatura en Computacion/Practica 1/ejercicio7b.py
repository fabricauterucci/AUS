def tablamultiplicar():
    n1= int(input("Ingrese un numero para saber su tabla de multiplicar "))
    p = n1 
    for x in range(11):
        p = n1* x
        print("La multiplicacion de",n1,"por ",x," es",p)

tablamultiplicar()
 
