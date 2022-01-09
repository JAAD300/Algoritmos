println("ingresa un número real a")
a = parse(Float64,readline())
println("ingresa un número real b, mayor o igual a",a)
b = parse(Float64,readline())
println("por último ingresa un número natural n")
n = parse(Int64, readline())
h = (b-a)/n
function j3(n)
    if n == 0
        println("la funnción j3(x) no está definida en x = 0")
    else
        return (15/(n^3) - 6/n)*(sin(n)/n) - (15/(n^2) - 1)*(cos(n)/n)
    end
end
println("el programa regresará los pares\nx, f(x)")
for i in range(a,stop = b,step = h)
    println((i, j3(i)))
    i = i + 1
end