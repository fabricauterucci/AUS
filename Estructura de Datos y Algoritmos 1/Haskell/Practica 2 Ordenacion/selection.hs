--- Selection Sort
delete x [] = []
delete x l = [y | y <- t, x /= y]


--- minimo devuelve el elemento minimo de la lista
minimo [x] = x
minimo (x:y:t) = if x < y then minimo(x:t)
 else minimo(y:t)


ssort [] = []
ssort [x] = [x]
ssort l = m: ssort l'
 where
 m = minimo l
 l' = delete m l