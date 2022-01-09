println("ingresa un número natural n")
n = parse(Int64,readline())
function formula(k)
    return ((2^k)*(factorial(big(k)))^2)/factorial(big(2*k + 1))
end
i = 0
suma = 0
while i <= n
    global i
    global suma
    suma = suma + formula(i)
    i = i + 1
end
print("el resultado, que aproxima a pi/2, es :",suma)