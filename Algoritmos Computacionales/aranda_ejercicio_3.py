n = int(input("ingresa un número natural n\n"))
def factorial(n):
    i = 0
    fac = 1
    while i < n:
        fac = fac*(n-i)
        i = i + 1
    return fac
def formula(k):
    return (2**k)*(factorial(k))**2/factorial(2*k + 1)
i = 0
suma = 0
while i <= n:
    suma = suma + formula(i)
    i = i + 1
print("el resultado, que aproxima a pi/2, es :",suma)