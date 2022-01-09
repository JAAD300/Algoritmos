println("ingresa un número natural n ≥ 3")
n = parse(Int64,readline())
j = 1
sumas = []
suma = 0
#hacemos las sumas y las agremos a una lista vacía. i va de 3 a n, y j va de 3 a i-2
for i in range(3,stop=n)
    while j <= i-2
        global suma
        global j
        suma = suma + (j + 3/4)^3 
        j = j +1
        append!(sumas, suma)
    end
end
#ahora hacemos la multiplicación de todas las sumas
producto = 1
for j in range(1,stop=length(sumas))
    global producto
    producto = producto*sumas[j]
end
println("el producto de las sumas es: ",producto) 