'''

Un grupo de científicos está
analizando una forma de vida inteligente extraterrestre en
la reconocida área 52. Han descubierto que, sorprendentemente,
estos usan las mismas letras que nosotros (26 letras, excluyendo la ñ)
aunque su alfabeto posee un orden distinto. Se nos encomienda la tarea
de reordenar un diccionario en español para que los extraterrestres puedan
buscar palabras en nuestra lengua más fácilmente. Diseñar un algoritmo que
dada un string que representa todas las letras del alfabeto ordenadas según
los extraterrestres y una lista de palabras, devuelva una lista de palabras
ordenadas (en el orden que entiendan los extraterrestres)


'''

# SIGNATURA: ordenar_extraterrestre : [String] -> String -> [String]
# La funcion toma una lista de palabras en con lenguaje humano, un alfabeto
# extraterrestre y traduce las palabras de lenguaje humano a lenguaje
# alienígena
def ordenar_extraterrestre(desordenadas, orden_alfabeto):
    #Definimos el orden del lenguaje humano
    Alfabeto_humano = 'abcdefghijklmnopqrstuvwxyz' 

    ordenada = [] #creamos una lista donde guardar las palabras ordenadas
                  # en lenguaje extraterrestre
    for palabra_desordenada in desordenadas: #Recorremos la lista de palabras en nuestro idioma
        palabra_ordenada = '' 
        for palabra_desordenada in palabra_desordenada.lower(): #en caso de haber mayusculas las convertimos
                                                                # en minusculas
            
            if palabra_desordenada in Alfabeto_humano: #si la letra esta en nuestro alfabeto, la convertimos al alfabeto extraterrestre
        # Identifica la posición de cada letra
                indice = Alfabeto_humano.index(palabra_desordenada) 
        # Añade una nueva letra al texto extraterrestre
                
                palabra_ordenada += orden_alfabeto[indice]
                
        ordenada += [palabra_ordenada] #una vez que la palabra esta completa, la agrega a la lista ordenada para los alienigenas

    return ordenada


#Utilizamos pytest mediante la funcion assert para verificar que los
#ejemplos descriptos en la documentación de la función
#se corresponden con el funcionamiento esperado.
#En caso de no funcionar,el compilador marca AssertionError
def test_ordenar_extraterrestre():
    #Testeamos los ejemplos de cadenas requeridos, con el alfabeto de los
    #extraterrestres en un orden distinto
    ordenada = ['revestir', 'miel', 'extraterrestre', 'auto', 'automovil', 'al']
    orden_alfabeto = 'zyxwvutsrqponmlkjihgfedcba'
    assert ordenar_extraterrestre(ordenada, orden_alfabeto) == ['ivevhgri', 'nrvo', 'vcgizgviivhgiv', 'zfgl', 'zfglnlero', 'zo']

    #Tambien testeamos el caso de no ingresar palabras, quiere decir
    #que su silencio es igual al de nosotros
    ordenada = []
    assert ordenar_extraterrestre(ordenada, orden_alfabeto) == []

    #Probamos el Algoritmo con otras cadenas
    ordenada = ['Yo','soy','tu','padre']
    assert ordenar_extraterrestre(ordenada, orden_alfabeto) == ['bl', 'hlb', 'gf', 'kzwiv']

    ordenada = ['PEDRITO','CLAVO','UN','CLAVITO']
    assert ordenar_extraterrestre(ordenada, orden_alfabeto) == ['kvwirgl', 'xozel', 'fm', 'xozergl']
    
    # y también con alfebeto de otros mundos
    orden_alfabeto = 'aaaaaaaaaaaaaaaaaaaaaaaaaa'
    assert ordenar_extraterrestre(ordenada, orden_alfabeto) == ['aa', 'aaa', 'aa', 'aaaaa']

    #Descomentar este ultimo codigo para que muestre el error de assertion
    #assert ordenar_extraterrestre(ordenada, orden_alfabeto) == ['aa', 'aaa', 'aa', 'aaaa']
    #el problema esta, en que en la ultima cadena falta una letra 'a'



#Fabrizio Alejandro Cauterucci
