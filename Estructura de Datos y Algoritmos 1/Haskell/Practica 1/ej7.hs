scalarproduct [] [] = 0
scalarproduct _ [] = 0
scalarproduct [] _ = 0
scalarproduct (x:xs) (y:ys) = x*y + scalarproduct xs ys
