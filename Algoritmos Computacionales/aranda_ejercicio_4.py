n = int(input("ingresa un número natural n\n"))
def BBP(k):
    return (1/16**k)*(4/(8*k + 1) - 2/(8*k + 4) - 1/(8*k + 5) - 1/(8*k + 6))
i = 0
suma = 0
while i <= n:
    suma = suma + BBP(i)
    i = i + 1
print("el resulatado de la fórmla BBP, que aproxima a pi, es:",suma)