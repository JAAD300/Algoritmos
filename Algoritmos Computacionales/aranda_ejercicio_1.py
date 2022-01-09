n = int(input("ingresa un número natural n\n"))
def leibniz(k):
    return ((-1)**k)/(2*k+1)
i = 0
suma = 0
while i <= n:
    suma = suma + leibniz(i)
    i = i + 1
print("el resulatado de la fórmula de Leibniz, que aproxima a pi/4, es:",suma)