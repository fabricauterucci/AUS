def ejercicio21():
    import math
    Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    UnidadM=["M","MC","MCC","MCCC","MCD","MD","MDC","MDCC","MDCCC","MCM"]
    N=int(input("Ingresa numero entero\n"))
    u= N % 10
    d=int(math.floor(N/10))%10
    c=int(math.floor(N/100))
    um=int(math.floor(N/1000))
    if(N>=1000): 
        print(Centena[c]+Decena[d]+Unidad[u]+UnidadM[um])
    else:
        if(N>=10):
            print(Decena[d]+Unidad[u])
        else:
            print(Unidad[N])

  
