--- Merge Sort
split [] = ([],[])
split [a] = ([a],[])
split (a:b:t) = (a:m, b:n)
 where
 (m,n) = split t
 
merge [] [] = []
merge a [] = a
merge [] b = b
merge (x:xs) (y:ys) = if x < y then (x: merge xs (y:ys))
                      else (y: merge (x:xs) ys)

msort [] = []
msort [x] = [x]
msort lista = let
              (i,j) = split lista
			  i' = msort i
			  j' = msort j
			  in
			    merge i' j'