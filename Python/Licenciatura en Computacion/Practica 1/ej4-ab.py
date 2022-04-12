
def per_rectangulo():
    base = float(input ("Ingrese la base del rectangulo "))
    altura = float(input ("Ingrese la altura del rectangulo "))

    Per = 2* base + 2* altura
    print( "EL perimetro del rectangulo es:",Per)
    



def area_rectangulo():
    base = float(input ("Ingrese la base del rectangulo "))
    altura = float(input ("Ingrese la altura del rectangulo "))

    Area = base * altura
    print("El area del rectangulo es:",Area)


def per_area_rectangulo():
    x1 = int(input ("Ingrese un punto x1 del rectangulo "))
    x2 = int(input ("Ingrese otro punto x2 del rectangulo "))
    y1 = int(input ("Ingrese otro punto y1 del rectangulo "))
    y2 = int(input ("Ingrese otro punto y2 del rectangulo "))

    base = abs(x2-x1)
    altura = abs(y2-y1)

    per_rectangulo1(base,altura)
    area_rectangulo1(base,altura)

def per_rectangulo1(base,altura):
    print('El perimetro es', (2*base+2*altura))

def area_rectangulo1(base,altura):
    print('El area es', (base*altura))

    

def per_circulo():
    r = int(input('Ingrese el radio del circulo'))
    pi = 3.141592
    per = 2*pi*r
    print("El perimetro del circulo es", per)

def area_circulo():
    r = int(input('Ingrese el radio del circulo'))
    pi = 3.141592
    area = (pi*r)**2
    print("El perimetro del circulo es", (pi*r)**2)

def hipo_triangulo():
    base = float(input("Ingrese la base del triangulo "))
    altura = float(input("Ingrese la altura del triangulo "))

    h = (base**2+altura**2)**1/2
    print("La hipotenusa del triangulo rectangulo es", h)


            

            
        
