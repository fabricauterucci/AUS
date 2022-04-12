def main():
    print("Qué desea hacer?\n")
    print("1)Calcular el perímetro de un rectángulo dada su base y su altura.\n")
    print("2)Calcular el área de un rectángulo dada su base y su altura.\n")
    print("3)Calcular el perímetro y el área de un rectángulo (alineado con los ejes x e y) dadas sus"
"coordenadas x1, x2, y1, y2.\n")
    
    x = int(input("Ingrese la opción que desea :"))

    if x == 1:
        perimetrorect()
    if x == 2:
        arearect()
    if x == 3:
        coord()
def perimetrorect():
    base = int(input("Ingrese la base de su rectangulo: "))
    altura = int(input("Ingrese la altura de su rectangulo: "))

    perimetro = 2*(base+altura)

    print("El perimetro del rectangulo es",perimetro)

def arearect():
    base = int(input("Ingrese la base de su rectangulo: "))
    altura = int(input("Ingrese la altura de su rectangulo: "))

    area = base*altura

    print("El area de su rectangulo es",area)

def coord():
    x1 = int(input("Ingrese la coordenada x1: "))
    x2 = int(input("Ingrese la coordenada x2: "))
    y1 = int(input("Ingrese la coordenada y1: "))
    y2 = int(input("Ingrese la coordenada y2: "))

    base = abs(x2-x1)
    altura = abs(y2-y1)

    per = peri(base,altura)
    are = area(base,altura)

    print("El perimetro es",per,"y el area es",are)
def peri(base,altura):
    return 2*(base+altura)


def area(base,altura):
    return (base*altura)
             

main()
