def segundos():
    h = int(input("Ingrese la cantidad de horas: "))
    m = int(input("Ingrese la cantidad de minutos: "))
    s = int(input("Ingrese la cantidad de segundos: "))

    h = h *60*60
    m = m*60

    print("El tiempo transcurrido en segundos es", h+m+s)


def hominseg():
    num=int(input("ingrese los segundos\n"))
    hor=(int(num/3600))
    minu=int((num-(hor*3600))/60)
    seg=num-((hor*3600)+(minu*60))
    print(str(hor)+"h "+str(minu)+"m "+str(seg)+"s")


hominseg()        
