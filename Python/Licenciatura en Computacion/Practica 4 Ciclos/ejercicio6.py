'''
Ejercicio 6. Escriba una función que reciba un número natural e imprima todos los números
primos que hay hasta ese número. Para esto se pide que:
a) Defina una función es_primo que toma un número natural y verifique si es un número
primo.
b) Resuelva el problema usando la función definida en el punto anterior.
'''

def es_primo(n):
    for i in range (2,n):
        if n%i == 0:
            return False
        else:
            return True

def ejercicio6(n):
     for x in range(1,n):
         if es_primo(x) == True:
             print(x)
    
        
    
        
    
