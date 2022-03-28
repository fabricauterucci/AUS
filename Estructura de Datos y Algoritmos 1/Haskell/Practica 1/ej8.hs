--- divisors, que dado un entero positivo x devuelve la lista de los divisores de x (y la lista vacı́a
--- si el entero no es positivo).

divisors n = [x | x <- [1..n], mod n x == 0  ]

--- Por comprension: [ f(x) / x pertenece a n]
--- es equivalente [ x | x <- [1..n], condicion]
--- significa que agrega a una lista, los x que cumplen
--- la condicion, x <- [1..n] crea y recorre una lista de 1 a n


--- matches, que dados un entero x y una lista de enteros descarta de la lista los elementos distintos
--- a x.


matches x xs = [ y | y <- xs, x /= y]


{- cuadrupla, que dados cuatro enteros a, b, c y d tales que 0 < a, b, c, d, ≤ 100, devuelve las
cuadruplas (a, b, c, d) que cumplen a^2 + b^2 = c^2 + d^2 .
-}

cuadrupla [a,b,c,d] = [ (a, b, c, d) | 0 < a && a <= 100,0 < b && b <= 100,0 < c && c <= 100,0 < d && d <= 100,  a**2+b**2 == c**2+d**2]
