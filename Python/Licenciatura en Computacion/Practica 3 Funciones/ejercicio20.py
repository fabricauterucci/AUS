'''
Ejercicio 20. Programa de astrología: el usuario debe ingresar el día y mes de su cumpleaños
y el programa le debe decir a qué signo corresponde.
Aries: 21 de marzo al 20 de abril. Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio. Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto. Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre. Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre. Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero. Piscis: 20 de febrero al 20 de marzo.



 
'''

def ejercicio20():
    d =int(input("Ingrese el dia de su cumpleaños: "))
    m =int(input("Ingrese el mes de su cumpleaños: "))
    if d<=0 or d>=32 or m<=0 or m>=13:
        print("\nError")

    if (d >=22 and d<=31):
        if m == 12:
            print("\nSu signo es Capricornio")
    if  (d>=1 and d<=20):
        if m == 1:
            print("\nSu signo es Capricornio")
    if (d >=21 and d<=31):
           if m == 1:
                print("\nSu signo es Acuario")
    if  (d>=1 and d<=19):
           if m == 2:
                print("\nSu signo es Acuario")
    if (d >=20 and d<=28):
           if m == 2:
                print("\nSu signo es Piscis")
    if  (d>=1 and d<=20):
           if m == 3:
                print("\nSu signo es Piscis")
    if (d >=21 and d<=31):
           if m == 3:
                print("\nSu signo es Aries")
    if  (d>=1 and d<=20):
           if m == 4:
                print("\nSu signo es Aries")
    if (d >=21 and d<=30):
           if m == 4:
                print("\nSu signo es Tauro")
    if  (d>=1 and d<=20):
           if m == 5:
                print("\nSu signo es Tauro")
    if (d >=21 and d<=31):
           if m == 5:
                print("\nSu signo es Geminis")
    if  (d>=1 and d<=21):
           if m == 6:
                print("\nSu signo es Geminis")
    if (d >=22 and d<=30):
           if m == 6:
                print("\nSu signo es Cancer")
    if  (d>=1 and d<=23):
           if m == 7:
                print("\nSu signo es Cancer")
    if (d >=24 and d<=31):
           if m == 7:
                print("\nSu signo es Leo")
    if  (d>=1 and d<=23):
           if m == 8:
                print("\nSu signo es Leo")
    if (d >=24 and d<=31):
           if m == 8:
                print("\nSu signo es Virgo")
    if  (d>=1 and d<=23):
           if m == 9:
                print("\nSu signo es Virgo")
    if (d >=24 and d<=30):
           if m == 9:
                print("\nSu signo es Libra")
    if  (d>=1 and d<=22):
           if m == 10:
                print("\nSu signo es Libra")
    if (d >=23 and d<=31):
           if m == 10:
                print("\nSu signo es Escorpio")
    if  (d>=1 and d<=22):
           if m == 11:
                print("\nSu signo es Escorpio")
    if (d >=23 and d<=30):
           if m == 11:
                print("\nSu signo es Sagitario")
    if  (d>=1 and d<=21):
           if m == 12:
                print("\nSu signo es Sagitario")
                
    

            

            

             
