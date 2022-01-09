println("ingresa un número natural n mayor o igual a 0")
n = parse(Int64, readline())
function a_k(k)
    if k == 0
        return sqrt(2)
    elseif k >= 1
        return sqrt(2 + a_k(k-1))
    else
        print("la sucesión sólo está definida para x = 0 ó x >= 1")
    end
end
print("el programa regresará el par k, a_k\nk a_k") 
k = 0
while k <= n + 1
    global k
    println((k,a_k(k)))
    k = k + 1
end