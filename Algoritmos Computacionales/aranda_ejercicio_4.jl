println("ingresa un número natural n")
n = parse(Int64,readline())
if n > 15
    println("A partir de n = 16 se produce un error de overflow\nk^16 se convierte en cero, lo que da como resultado Inf")
end
function BBP(k)
    return (4/(8*k + 1) - 2/(8*k + 4) - 1/(8*k + 5) - 1/(8*k + 6))/(16^k)
end
i = 0
suma = 0
while i <= n
    global i
    global suma
    suma = suma + BBP(i)
    i = i + 1
end
print("el resulatado de la fórmla BBP, que aproxima a pi, es:",suma)
