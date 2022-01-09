import numpy as np
a = float(input("ingresa un número real a\n"))
b = float(input("{} {}".format('ingresa un número real b, mayor o igual a',a)+"\n"))
n = int(input("por último ingresa un número natural n\n"))
def j3(n):
    if n == 0:
        print('la funnción j3(x) no está definida en x = 0')
    else:
        return (15/(n**3) - 6/n)*(np.sin(n)/n) - (15/(n**2) - 1)*(np.cos(n)/n)
print("el programa regresará los pares x, f(x)\n{0:^5}  {1:^5}".format("x","f(x)")) 
for i in np.linspace(a,b,n+1): #el n+1 es para que (a_i+1) - (a_i) = (b-a)/n
    if i == 0:
        print(j3(0))
    else:
        print("{0:^5.5}, {1:^5.5}".format(i,j3(i)))