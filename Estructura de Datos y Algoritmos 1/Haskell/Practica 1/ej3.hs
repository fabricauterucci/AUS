--- Reescribir sin usar let, where, if

--- f x = let (y,z) = (x,x) in y

f x = x


--- greater (x,y) = if x > y then True else False
greater (x,y) = if x > y then True else False

greater (x,y) |  x > y = True
              |  otherwise = False
			  
--- f (x,y) = let z = x + y in g (z,y) where g (a,b) = a − b

f2 (x,y) = x

f3 (x,y) = let z = x + y in g (z,y)
           where g (a,b) = (a - b)