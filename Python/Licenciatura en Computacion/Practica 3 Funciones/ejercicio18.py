'''
Ejercicio 18. Modificar el programa anterior para satisfacer los siguientes requerimientos:
a) Se diferencia una categoría más, ahora si la temperatura esta entre 25 y 32 grados el
mensaje deberá ser “Caluroso", pero si la temperatura excede los 32 grados deberá decir
"Muy caluroso".
b) Se establece un nuevo criterio de clasificación:
Intervalo Denominación
menos de 0 grados "Helado"
entre 0 y 10 grados "Frío"
entre 10 y 15 grados “Fresco”
entre 15 y 25 grados “Agradable”
entre 15 y 25 grados “Caluroso”
más de 32 grados “ Muy Caluroso”
Modificar el programa para que se adapte a este cambio.
c) El programa ahora deberá avisarnos si es necesario utilizar protector solar o no. Para ello,
se sabe que, si la temperatura es menor a los 15 no es necesario utilizar protector solar,
pero por el contrario si la temperatura supera dicho valor, si se debe utilizar protector.
'''

def ejercicio18():
    c = int(input("Ingrese los grados centigrados: "))

    if c< 0:
        print("El clima esta Helado\n")
    if c>= 0 and c<= 15:
        print("El clima esta Frío\n")
    if c>15 and c<= 25:
        print("El clima esta Agradable\n")
    if c>25 and c<=32:
        print("El clima esta Caluroso\n")
    if c>32:
        print("El clima esta insoportable\n")
    if c<=15:
        print("No es necesario usar protector solar")
    if c>15:
        print("Es necesario usar protector solar")

ejercicio18()

