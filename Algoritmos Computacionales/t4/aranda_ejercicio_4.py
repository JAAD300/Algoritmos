print("tienes que ingresar 3 números reales, a, b, k")
a = float(input("ingresa el primer número a\n"))
print("ingresa el segundo número b, b mayor a", a)
b = float(input())
print("ingresa el tercer número k, tal que 0 < k <",b-a)
k = float(input())
print("el programa mostrará los números r tales que\na ≤ r ≤ b, r = a + n*k, n natural")
#r = a + n*k <= b, entonces n <= (b - a)/k
i = 0
while i <= (b - a)/k: 
    r = a + i*k
    print(r)
    i += 1
