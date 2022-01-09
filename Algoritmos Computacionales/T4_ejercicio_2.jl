println("ingresa un número natural n")
n = parse(Int64,readline())
#calculamos la cota superior
límite_sup = 3*n^2 + 2*n + 5
println("3n^2 + 2n + 5 = límite superior = ",límite_sup)
println("los números m múltiplos de 5 o 7 y que cumplen que 1 <= m <= 3n^2 + 2n + 5 son:")
#vemos qué números son múltiplos de 5 o de 7 y los "imprimimos"
for i in range(1,stop=límite_sup)
    if i%5 == 0
        println(i)
    elseif i%7 == 0
        println(i)
    end
end