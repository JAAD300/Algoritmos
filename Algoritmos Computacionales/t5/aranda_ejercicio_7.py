import numpy as np
a = float(input("ingresa un número real a\n"))
b = float(input("{} {}".format('ingresa un número real b, mayor o igual a',a)+"\n"))
n = int(input("por último ingresa un número natural n\n"))
def arcsch(x): #arcschx ≡ ln[1/x + √(1/x2 + 1)], arco cosecante hiperbólica 
    if x == 0:
        print('la funnción arcsch(x) no está definida en x = 0')
    else:
        return np.log(1/x + np.sqrt(1/x**2 + 1))
print("el programa regresará los pares x, f(x)\n{0:^5}  {1:^5}".format("x","f(x)")) 
for i in np.linspace(a,b,n+1): #el n+1 es para que (a_i+1) - (a_i) = (b-a)/n
    if i == 0:
        print(arcsch(0))
    else:
        print("{0:^5.5}, {1:^5.5}".format(i,arcsch(i)))