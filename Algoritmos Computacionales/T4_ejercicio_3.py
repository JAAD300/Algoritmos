n = int(input("ingresa un número natural n ≥ 3\n"))
j = 1
sumas = []
suma = 0
#hacemos las sumas y las agremos a una lista vacía. i va de 3 a n, y j va de 3 a i-2
for i in range(3,n+1): #se pone n+1, pues en el range(3,5) i toma los valores 3 y 4
    while j <= i-2:
        suma = suma + (j + 3/4)**3 
        j = j +1
        sumas.append(suma)
#print("las sumas son:",sumas)
#ahora hacemos la multiplicación de todas las sumas
producto = 1
for j in range(0,len(sumas)):
    producto = producto*sumas[j]
print("el producto de las sumas es: ",producto) 