
--- Colocamos n-1 en divisores porque quiero excluir el propio numero

--- Analogamente, en perfectos, pongo m-1 porque la consigna dice numeros perfectos menores que n

---

divisores :: Integral t => t -> [t]

divisores n = [ x| x <- [1..n-1], (mod n x == 0)]

---
suma :: Num a => [a] -> a

suma [] = 0
suma (x:t) = x + suma t
---
perfectos :: Integral t => t -> [t]

perfectos m = [x | x <-[1..m-1],x == suma(divisores x)]
