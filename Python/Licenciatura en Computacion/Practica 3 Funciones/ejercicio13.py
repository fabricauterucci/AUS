'''Usando las funciones del ejercicio anterior, escribir un programa que pida al
usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y
muestre por pantalla la duración total en horas, minutos, y segundos.
'''


def pasaasegundos(h,m,s):
    h = h *60*60
    m = m*60
    return h+m+s

      
def segundos():
    h = int(input("Ingrese la cantidad de horas: "))
    m = int(input("Ingrese la cantidad de minutos: "))
    s = int(input("Ingrese la cantidad de segundos: "))


    print("El tiempo transcurrido en segundos es", auxiliar(h,m,s))





def hominseg():
    num=int(input("ingrese la cantidad de segundos: \n"))

    auxhominseg(num)
    

def auxhominseg(num):
    
    hor=(int(num/3600))
    minu=int((num-(hor*3600))/60)
    seg=num-((hor*3600)+(minu*60))
    return(str(hor)+"h "+str(minu)+"m "+str(seg)+"s")



def ejercicio13():
    print("Ingrese dos horas distintas(en horas, minutos y segundos)")
    h1 = int(input("Ingrese la cantidad de horas del primer tiempo: \n"))
    m1 = int(input("Ingrese la cantidad de minutos del primer tiempo: \n"))
    s1 = int(input("Ingrese la cantidad de segundos del primer tiempo: \n"))
    h2 = int(input("Ingrese la cantidad de horas del segundo tiempo: \n"))
    m2 = int(input("Ingrese la cantidad de minutos del segundo tiempo: \n"))
    s2 = int(input("Ingrese la cantidad de segundos del segundo tiempo: \n"))

    hora1 = pasaasegundos(h1,m1,s1)
    hora2 = pasaasegundos(h1,m1,s1)
    numero = hora1+hora2

    print (auxhominseg(numero))
ejercicio13()



