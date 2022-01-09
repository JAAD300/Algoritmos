println("ingresa un número natural n")
n = parse(Int64,readline())
function basel(k)
    return 1/(k^2)
end
i = 1
suma = 0
while i <= n
    global suma
    global i
    suma = suma + basel(i)
    i = i + 1
end
print("el resulatado del problema de Basel, que aproxima a (pi^2)/6, es:",suma)
