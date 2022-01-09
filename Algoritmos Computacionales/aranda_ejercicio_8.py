import numpy as np
n = int(input("ingresa un número natural n mayor o igual a 0\n"))
def a_k(k):
    if k == 0:
        return np.sqrt(2)
    elif k >= 1:
        return np.sqrt(2 + a_k(k-1))
    else:
        print('la sucesión sólo está definida para x = 0 ó x >= 1')
print("el programa regresará el par k, a_k\n{}  {}".format('k','a_k')) 
k = 0
while k <= n + 1:
    print('{}, {}'.format(k,a_k(k)))
    k = k + 1