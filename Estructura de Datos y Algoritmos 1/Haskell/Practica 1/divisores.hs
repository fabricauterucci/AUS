divisores n = [x | x<-[1..n], (n`mod`x)==0]

divisores' 0 = []
divisores' n = buscadivisores [1..n]
  where
    buscadivisores [] = []
    buscadivisores (x:t) = if (n`mod`x)== 0 then x:(buscadivisores t)
                           else buscadivisores t
--- divisores 4 ------>> buscadivisores [1..4]---
--- 1: buscadivisores [2,3,4] ---> 1:2:buscadivisores [3,4]---->
---
--- 1:2:buscadivisores [4]------>
---
--- 1:2:4:buscadivisores []
---
--- 1:2:4:[]
--- devolver una tupla
--- el primer elemento de la tupla son los divisores
--- el segundo elemento son los no divisores.
partir n = ( [x | x<-[1..n], (n`mod`x)==0], [x | x<-[1..n], (n`mod`x) /= 0])
partir' 0 = ([],[])
partir' n = bf [1..n]
  where bf [] = ([],[])
        bf (x:t) = let (div,no_div) = bf t in if (n `mod` x) == 0 then (x:div, no_div)
                                        else (div, x:no_div)
--- bf [] = ([], [])
--- bf (x:t) = if (n `mod` x) == 0 then (x:div, no_div)
---  else (div, x: no_div)
---where (div, no_div) = bf t

cuenta [] = 0
cuenta (x:t) = 1 + cuenta t
primos m = [x | x<-[1..m], cuenta(divisores x) == 2]

prime n = divisores n == [1,n]