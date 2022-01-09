import numpy as np
n = int(input("ingresa un número natural n mayor o igual a 0\n"))
def H_n(k):
    if k == 1:
        return 1
    elif k == 2:
        return 6
    else:
        return k*(H_n(k-1))
        #print('la sucesión sólo está definida para x = 0 ó x >= 1')
print("el programa regresará el par k, a_k\n{}  {}".format('k','a_k')) 
k = 1
while k <= n + 1:
    print('{}, {}'.format(k,H_n(k)))
    k = k + 1