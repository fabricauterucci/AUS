---
insertar:: (Ord a)=> a->[a]->[a]

insertar x [] = [x]
insertar x (y:ys) = if x <= y then x:y:ys
                    else y:insertar x ys

particion :: Ord a => a->[a]->([a],[a])

particion x [] = ([],[])
particion x (y:ys) = if y <= x then (y:min,may)
                     else (min,y:may)
                     where
                     (min,may) = particion x ys


qsort::(Ord a)=>[a]->[a]

qsort [] = []
qsort [z] = [z]
qsort (z:zs) = qsort min ++ [z] ++ qsort may
  where (min,may) = particion z zs
