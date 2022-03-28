--- Quick Sort
qsort [] = []
qsort [x] = [x]
qsort (x:t) = qsort menores ++ [x] ++ qsort mayores
 where
 menores l = [ y | y <- l, y < x ]
 mayoores l = [ y | y <- l, x <= y ]