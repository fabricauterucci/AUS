'''
Ejercicio 17. Definir la función observar_clima la cual clasifica con una “etiqueta” ciertos
intervalos numéricos asociados a temperaturas ambientes. La categorización de las tempera-
turas es la siguiente:
Intervalo Denominación
menos de 0 grados "Helado"
entre 0 y 15 grados "Frío"
entre 15 y 25 grados “Agradable”
más de 25 grados “Caluroso”
'''

def ejercicio18():
    c = int(input("Ingrese los grados centigrados: "))

    if c< 0:
        print("El clima esta Helado\n")
    if c>= 0 and c<= 15:
        print("El clima esta Frío\n")
    if c>15 and c<= 25:
        print("El clima esta Agradable\n")
    if c>25:
        print("El clima esta Caluroso\n")
  

ejercicio17()
