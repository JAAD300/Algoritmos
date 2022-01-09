println("tienes que ingresar 3 números reales, a, b, k\ningresa el primer número a")
a = parse(Float64, readline())
println("ingresa el segundo número b, b mayor a ", a)
b = parse(Float64, readline())
println("ingresa el tercer número k, tal que 0 < k < ",b-a)
k = parse(Float64, readline())
println("el programa mostrará los números r tales que\na ≤ r ≤ b, r = a + n*k, n natural")
#r = a + n*k <= b, entonces n <= (b - a)/k
i = 0
while i <= (b - a)/k
    global i
    r = a + i*k
    println(r)
    i = i + 1
end