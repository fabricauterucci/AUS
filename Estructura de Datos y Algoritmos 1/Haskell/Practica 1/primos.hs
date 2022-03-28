cuenta [] = 0
cuenta (x:t) = 1 + cuenta t

primos m = [ x | x <-[1..m], cuenta(divisores x) == 2 ]



prime n = divisores n == [1,n]
