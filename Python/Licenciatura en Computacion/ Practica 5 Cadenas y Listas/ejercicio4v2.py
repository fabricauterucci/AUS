'''
4) Escriba un programa que contenga la función que reciba como parámetro una cadena de
palabras separadas por espacios y devuelva, como resultado, cuántas palabras de más
de cinco letras tiene la cadena dada.
'''


def ej4(cadena):
    count = 0
    contadordeletras = 0
    cuentapalabras = 0
    ultimocontador = 0
    

    for x  in cadena :
        if x != ' ':
            contadordeletras += 1
                        
        if contadordeletras < 5 and x == ' ':
            contadordeletras = 0
            
        if contadordeletras >= 5 and x == ' ':
            cuentapalabras +=1
            contadordeletras = 0
            
       
        ultimocontador += 1
        if contadordeletras >= 5 and ultimocontador == len(cadena):
            cuentapalabras +=1
        
            
    print("La cantidad de palabras con cinco o más letras es", cuentapalabras)
    
    

               
            
        

