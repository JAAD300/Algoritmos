import numpy as np
print("\ncalcularemos la cantidad de bits necesarios, k, para\nrepresentar el número m = (13^2n)(23^(n^2))")
n=int(input("\ningresa un número natural n\n"))
#a = 13**(2*n),b = 23**(n**2), m = a*b
c = 2*n*np.log2(13)
d = (n**2)*np.log2(23)
if n == 0:
    print("\nel número de bits necesarios, k, para representar a m es: 1")
else:
    k = np.floor(c + d)
    print("\nel número de bits necesarios, k, para representar a m es: ",k)
print("")