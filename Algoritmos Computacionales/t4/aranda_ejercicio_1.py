import numpy as np
n = int(input("Ingresa un número natural n mayor o igual a 1\n"))
print("n^2=",n**2)
#calculamos los ln(3k+1) y los guardamos es una lista vacía Logs
Logs = []
i = 1
while i <= n**2:
    Logs.append(np.log(3*i+1))
    i = i + 1
#hacemos el producto de los ln(3k+1) guardados en la lista Logs 
producto = 1
for j in range(0,len(Logs)):
    producto = producto*Logs[j]
print("La multiplicación de los ln(3k+1) desde k = 1 hasta k = n^2 es:\n",producto)