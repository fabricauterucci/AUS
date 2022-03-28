--- five dado cualquier valor devuelve 5
five n = 5

--- apply, que toma una función y un valor, y devuelve el resultado de aplicar la funciónal valor
--- dado

apply f n = f(n)

--- identi es la funcion identidad
identi x = x

--- first toma un par ordenado y devuelve su primer componente
first (x,y) = x

--- La funcion sign devuelve 1 si es positivo, -1 si es negativo
--- 0 en caso contrario
sign x = if x > 0 then 1
        else if x < 0 then -1
        else 0

--- abs, la función valor absoluto (usando sign y sin usarla)
abso n = if n >= 0 then n
        else (sign n) * n
		
--- pot, que toma un entero y un número, y devuelve el resultado de elevar el segundo a la
--- potencia dada por el primero
pot 0 x = 1
pot 1 x = x
pot 2 x = x * x
pot n x = x * (pot (n-1) x)

--- XOR es el equivalente distinto

xor a b = if a == b then 0
          else 1
		  
--- max2 toma 2 numeros y devuelve el maximo
max2 a b = if a >= b then a
           else b

--- max 3 toma 3 numeros y devuelve el maximo
max3 a b c = max2 (max2 a b) c

---swap que toma un par y devuelve el par invertido
swap(a,b) = (b,a)