def hola(nombre):
    return 'Hola ' + nombre +'!'

def saludo():
    nombre = input(' Por favor ingrese su nombre ')
    saludar = hola(nombre)

    print(saludar)

saludo()
