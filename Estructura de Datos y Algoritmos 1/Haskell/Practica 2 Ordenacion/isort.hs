--- Insertion Sort
insert x [] = [x]
insert x (y:t) = if x < y then (x:y:t)
                 else (y: (insert x t))

isort [] = []
isort [x] = [x]
isort (x:t) = insert x (isort t)