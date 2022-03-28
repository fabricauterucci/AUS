newtype ArbolBin a = Empty | Nodo a (ArbolBin a) (ArbolBin a) deriving Show
---addTree   :: (Ord a) => a -> ArbolBin a -> ArbolBin a

addTree x Empty = (Nodo x) (Empty) (Empty)
addTree x ((Nodo a) lt rt )| x == y = ((Nodo a) (lt) (rt))
                           | x < y  = ((Nodo a) (addTree x (lt)) (rt))
                           | x > y = ((Nodo a) (lt) (addTree x (rt)))

---inOrderTree     :: (Ord a)=> ArbolBin a -> [a]
inOrderTree Empty = []
inOrderTree ((Nodo a) lt rt) = inOrderTree lt ++ [a] ++ inOrderTree rt
