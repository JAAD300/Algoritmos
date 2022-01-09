println("ingresa un número natural n")
n = parse(Int64,readline())
function leibniz(k)
    return ((-1)^k)/(2*k+1)
end
i = 0
suma = 0
while i <= n
    global suma
    global i
    suma = suma + leibniz(i)
    i = i + 1
end
print("el resulatado de la fórmula de Leibniz, que aproxima a pi/4, es:",suma)