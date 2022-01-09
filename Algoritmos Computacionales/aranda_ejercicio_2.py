n = int(input("ingresa un número natural n\n"))
def basel(k):
    return 1/(k**2)
i = 1
suma = 0
while i <= n:
    suma = suma + basel(i)
    i = i + 1
print("el resulatado del problema de Basel, que aproxima a (pi^2)/6, es:",suma)