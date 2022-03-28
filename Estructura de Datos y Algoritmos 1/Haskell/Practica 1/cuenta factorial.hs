fact 0 = 1
fact n = n * fact(n-1) 

--- Contar cantidad de elementos en lista
cuenta [] = 0
cuenta (x:t) = 1 + cuenta t

--- Sumar elementos de una lista
sumar [] = 0
sumar (x:t) = x + sumar t

--- Revertir los elementos de una lista
rev [] = []
rev [x] = [x]
rev (x:xs) = rev xs ++ [x]

--- Concatenar dos listas

concat l1 [] = l1
concat [] l2 = l2
concat (x:xs) l2 = x: concat xs l2