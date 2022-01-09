n = int(input("ingresa un número natural n\n"))
#calculamos la cota superior
cota_sup = 3*n**2 + 2*n + 5
print("\n3n^2 + 2n + 5 = límite superior = ",cota_sup)
print("\nlos números m múltiplos de 5 o 7 y que cumplen que 1 <= m <= 3n^2 + 2n + 5 son:\n")
#vemos qué números son múltiplos de 5 o de 7 y los "imprimimos"
for i in range(1,cota_sup):
    if i%5 == 0:
        print(i)
    elif i%7 == 0:
        print(i)