def separador():
    n = int(input("¿Cuantos espacios desea separar entre las repeticiones? "))
    c = input("Ingrese una palabra para ser repetida")
    for x in range (1,10031):
        print(c,end=' '*n)

separador()
