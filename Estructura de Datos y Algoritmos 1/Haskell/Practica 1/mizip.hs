mizip [] _ = []
mizip _ [] = []
mizip (x:xs)(y:ys) = (x,y): mizip xs ys

--- zip de biblioteca hace lo mismo

addyascentes [] = []
addyascentes (x:xs) = mizip (x:xs) xs

addy y = zip y (tail y)

f t = [ x <= y | (x,y) <- addy t]

miAnd [] = True
miAnd [x] = x
miAnd [x:t] = x && miAnd t