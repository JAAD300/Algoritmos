println("Ingresa un número natural n mayor o igual a 1")
n = parse(Int64,readline())
println("n^2=",n^2)
#calculamos los ln(3k+1) y los guardamos es una lista vacía Logs
Logs = []
i = 1
while i <= n^2
    global i
    append!(Logs, log(3*i+1))
    #Logs.append(log(3*i+1))
    i = i + 1
end    
#hacemos el producto de los ln(3k+1) guardados en la lista Logs 
producto = 1
for j in range(1,stop=length(Logs))
    global producto
    producto = producto*Logs[j]
end
println("La multiplicación de los ln(3k+1) desde k = 1 hasta k = n^2 es:\n",producto)