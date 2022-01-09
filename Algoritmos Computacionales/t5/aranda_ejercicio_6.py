import numpy as np
a = float(input("ingresa un número real a\n"))
b = float(input("{} {}".format('ingresa un número real b, mayor o igual a',a)+"\n"))
n = int(input("por último ingresa un número natural n\n"))
def hermite(x):
    if x < 0:
        return 512*x**9 - 9216*x**7 + 48384*x**5 - 80640*x**3 + 30240*x
    else:
        return 128*x**7 - 1344*x**5 + 3360*x**3 - 680*x
print("el programa regresará los pares x, f(x)\n{0:^5}  {1:^5}".format("x","f(x)")) 
for i in np.linspace(a,b,n+1): #el n+1 es para que (a_i+1) - (a_i) = (b-a)/n
    print("{0:^5.5}, {1:^5.5}".format(i,hermite(i)))