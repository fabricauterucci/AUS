'''
2) El tiempo como tuplas
a) Proponer una representación con tuplas para representar el tiempo.
b) Escribir una función sumaTiempo que reciba dos tiempos dados y devuelva su suma
'''

def tiempo():
    tiempo = ()
    tiempo1 = ()
    
    h = int(input("Ingrese la hora"))
    m = int(input("Ingrese un minuto"))
    s = int(input("Ingrese los segundos"))


    tiempo1 = (h,m,s)
    tiempo = (h,"h",m,"min",s,"seg")

    

    print(tiempo)
    

def aux(x,y,z,):
    tiempo = (x,"h",y,"min",z,"seg")
    print(tiempo)

    
def sumaTiempo(tiempo = (),tiempo2 = ()):

    
    h = int(input("Ingrese la hora"))
    m = int(input("Ingrese un minuto"))
    s = int(input("Ingrese los segundos"))    

 

    h1 = int(input("Ingrese la hora"))
    m1 = int(input("Ingrese un minuto"))
    s1 = int(input("Ingrese los segundos"))

 

    count = 0

    segundos = s1+s
    minutos = m1+m

        
   
    while segundos >= 60:
        segundos = segundos-60
        count += 1
        if segundos < 60:
            minutos = m1+m+count
            count = 0
    if s1+s >= 0 and s1+s < 60 :
        minutos = m1+m
        segundos = s1+s

    
    

    while minutos >= 60:
        minutos = minutos-60
        count += 1
        if minutos < 60:
            horas = h1+h+count
    if minutos >= 0 and minutos < 60 :
        horas = h1+h
        
        
        tiempo = horas,minutos,segundos,

        aux(horas,minutos,segundos,)



        
    
        
    
    
