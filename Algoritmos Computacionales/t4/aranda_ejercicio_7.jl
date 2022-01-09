print("ingresa un número real a")
a = parse(Float64,readline())
println("ingresa un número real b, mayor o igual a",a)
b = parse(Float64,readline())
println("por último ingresa un número natural n")
n = parse(Int64, readline())
h = (b-a)/n
function arcsch(x) #arcschx ≡ ln[1/x + √(1/x2 + 1)], arco cosecante hiperbólica 
    if x == 0
        print("la funnción arcsch(x) no está definida en x = 0")
    else
        return log(1/x + sqrt(1/x^2 + 1))
    end
end
println("el programa regresará los pares\nx, f(x)") 
for i in range(a, stop = b, step = h)
    println((i,arcsch(i)))
end