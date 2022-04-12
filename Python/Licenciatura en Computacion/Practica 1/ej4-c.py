def per_area_rectangulo():
    x1 = int(input ("Ingrese un punto del rectangulo "))
    x2 = int(input ("Ingrese otro punto cercano al anterior "))
    y1 = int(input ("Ingrese otro punto lejano al anterior "))
    y2 = int(input ("Ingrese otro punto cercano al anterior "))
    
    Per = 2* (x1+y1) + 2* (x1+x2)
    Area = (x2+y1) * (x1+x2)
    print( "EL perimetro del rectangulo es:")
    print (Per)

    print("El area del rectangulo es:")
    print(Area)

per_rectangulo()
 #preguntar x e y binario
