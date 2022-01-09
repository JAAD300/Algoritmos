print("ingresa un número real a")
a = parse(Float64,readline())
println("ingresa un número real b, mayor o igual a",a)
b = parse(Float64,readline())
println("por último ingresa un número natural n")
n = parse(Int64, readline())
h = (b-a)/n
function hermite(x)
    if x < 0
        return 512*x^9 - 9216*x^7 + 48384*x^5 - 80640*x^3 + 30240*x
    else
        return 128*x^7 - 1344*x^5 + 3360*x^3 - 680*x
    end
end
println("el programa regresará los pares\nx, f(x)") 
for i in range(a,stop = b,step = h) #el n+1 es para que (a_i+1) - (a_i) = (b-a)/n
    println((i,hermite(i)))
end