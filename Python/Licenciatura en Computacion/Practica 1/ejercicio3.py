# -*- encoding: utf-8 -*-

def ejercicio3():
    """
        Preguntará el nombre del usuario,
        luego preguntará dos números e imprimirá el resultado.
        Args:
            La función no posee argumentos
        Returns:
            La función no posee valor de retorno
    """
    nombre = input("Seamos cordiales, ¿cómo se llama usted? ")
    # Esto es un comentario. El caracter \n corresponde a una linea en blanco.
    # por lo que el saludo será precedido y finalizado con líneas en blanco
    print("\nHola, " + nombre + " encantado, yo soy Python 3.4\n")
    print(nombre, ", vamos a mostrar lo que podemos hacer...")
    numero1 = input("Ingrese un número por favor: ")
    numero2 = input("Ahora, ingrese otro número: ")
    print("Ahora vamos a obtener el prodcto de ", numero1, " y ", numero2)
    # Dentro de los argumentos de la función print podemos utilizar expresiones
    # En este caso se asume que los valores ingresados corresponden a números
    # enteros por lo que para poder multiplicarlos debemos indicarle al sistema
    # que los haga "convirtiéndo" el string ingresado a entero
    print("Gracias al poder de Python podemos saber que: ", numero1, 'x', numero2, '= ', int(numero1) * int(numero2))
    print("¡Tada!")


# Llamamos a la función definida arriba
ejercicio3()
