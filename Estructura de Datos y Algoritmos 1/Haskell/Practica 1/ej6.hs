import Data.Char
--- suma, que suma todos los elementos de una lista de números

suma [] = 0
suma [x] = x
suma (x:xs) = x + suma(xs)


--- alguno, que devuelve True si algún elemento de una lista de valores booleanos es True, y
--- False en caso contrario
alguno [] = False
alguno [False] = False
alguno (x:xs) = if ( x == True) then True
                else alguno(xs)

--- todos, que devuelve True si todos los elementos de una lista de valores booleanos son True,
--- y False en caso contrario
todos [] = False
todos [True] = True
todos lista = and lista 

--- codes, que dada una lista de caracteres,
--- devuelve la lista de sus ordinales
codes [] = []
codes (x:xs) = [ord x] ++ codes(xs)

--- restos, que calcula la lista de los restos de la división de los elementos de una lista de
--- números dada por otro número dado

restos [] x = []
restos (y:ys) x = [mod y x] ++ restos ys x



--- cuadrados, que dada una lista de números,
--- devuelva la lista de sus cuadrados

cuadrados [] = []
cuadrados (x:xs) = [round(x**2)] ++ cuadrados xs

--- longitudes, que dada una lista de listas,
--- devuelve la lista de sus longitudes

longitudes [] = 0
longitudes (x:xs) = 1 + longitudes xs



--- orden, que dada una lista de pares de números, devuelve la lista de aquellos pares en los
--- que la primera componente es menor que el triple de la segunda

orden [] = []
orden [(x,y)] = if x < (3 * y)
  then [(x,y)]
  else []
orden (z:zs) =  orden [z] ++ orden zs

--- pares, que dada una lista de enteros,
--- devuelve la lista de los elementos pares

pares [] = []
pares [x] = if mod x 2 == 0
  then [x]
  else []
pares (x:xs) = pares [x] ++ pares xs



--- letras, que dada una lista de caracteres, devuelve la lista de aquellos que son letras
--- (minúsculas o mayúsculas)

letras [] = []
letras [x] = if isDigit x == False
  then [x]
  else []
letras (x:xs) = letras [x] ++ letras xs

---masDe, que dada una lista de listas xss y un número n, devuelve la lista de aquellas listas
---de xss con longitud mayor que n

masDe [] n = []

masDe (x:xs) n = if ((longitudes x) > n)
  then (x ++ masDe xs n)
  else (masDe xs n)























