println("\ncalcularemos la cantidad de bits necesarios, k, para\nrepresentar el número m = (13^2n)(23^(n^2))")
println("\ningresa un número natural n")
n = parse(Int64, readline())
#a = 13**(2*n),b = 23**(n**2), m = a*b
c = 2*n*log2(13)
d = (n^2)*log2(23)
if n == 0
    print("el número de bits necesarios, k, para representar a m es: 1")
else
    k = floor(c + d)
    print("el número de bits necesarios, k, para representar a m es: ",k)
end
println("\n") 