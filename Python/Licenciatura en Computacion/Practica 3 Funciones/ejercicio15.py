'''a) Escribir una función que dado un vector al origen (definido por sus coordenadas (x, y),
devuelva la norma del vector, dada por ||(x, y)|| = (x**2 + y**2)^1/2
'''

def normal(x,y):
    normal = float((x**2 + y**2)**(1/2))
    return normal    
    
def ejercicio15a():
    x = float(input("Ingrese la coordenada del eje x :"))
    y = float(input("Ingrese la coordenada del eje y :"))

    print("El vector normal es", normal(x,y))

'''
Utilizando las funciones anteriores, escribir una función que dados dos puntos en el plano
(x 1 , y 1 ) y (x 2 , y 2 ), devuelva la distancia entre ambos
'''    

def ejercicio15b():
    x1 = float(input("Ingrese la primer coordenada del eje x del primer punto: "))
    y1 = float(input("Ingrese la segunda coordenada del eje y del primer punto: "))
    x2 = float(input("Ingrese la primer coordenada del eje x del segundo punto: "))
    y2 = float(input("Ingrese la segunda coordenada del eje y del segundo punto: "))

    segmentocoord1 = x2-x1
    segmentocoord2 = y2-y1

    
    
    print("La distancia entre ambos es",normal(segmentocoord1,segmentocoord2))

'''
Escribir una función que calcule el área de un triángulo a partir de su base y su altura.
'''

def ejercicio15c(base,altura):
    return (base*altura)/2

'''
Utilizando las funciones anteriores escribir una función que reciba tres puntos en el plano
(x 1 , y 1 ), (x 2 , y 2 ), y (x 3 , y 3 ), y devuelva el área del triángulo correspondiente.

'''




def ejercicio15d():
    x1 = float(input("Ingrese la primer coordenada del eje x del primer punto: "))
    y1 = float(input("Ingrese la segunda coordenada del eje y del primer punto: "))
    x2 = float(input("Ingrese la primer coordenada del eje x del segundo punto: "))
    y2 = float(input("Ingrese la segunda coordenada del eje y del segundo punto: "))
    x3 = float(input("Ingrese la tercer coordenada del eje x del tercer punto: "))
    y3 = float(input("Ingrese la tercer coordenada del eje y del tercer punto: "))

    segmentocoord1 = x2-x1
    segmentocoord2 = y2-y1
    promedio1 = (x1+x2)/2
    promedio2 = (y1+y2)/2
    
    
    base1 = normal(segmentocoord1,segmentocoord2) #segmento de la base
    altura1 = normal(x3-promedio1,y3-promedio2) #segmento del punto medio de la base, con el punto restante

    ejercicio15c(base1,altura1)
    print("La base del triangulo es", ejercicio15c(base1,altura1))

ejercicio15d()
    
    
    



    
