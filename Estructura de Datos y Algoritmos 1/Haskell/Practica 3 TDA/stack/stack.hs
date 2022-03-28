newtype Stack a   = Stk [a] deriving Show

push x (Stk xs)   = Stk (x:xs)

pop (Stk [])      = error "Stack Vacio"
pop (Stk (_:xs)) = Stk xs

top (Stk []) = error "Stack Vacio"
top (Stk (x:_)) = x

emptyStk = Stk []
stackIsEmpty(Stk []) = True
stackIsEmpty(Stk _) = False

