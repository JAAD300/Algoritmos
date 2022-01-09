import numpy as np 
print("Calcularemos el volumen de una esfera\nCuál es el radio r de la esfera?")
r=float(input())
print("la clase de r es:",type(r))
v=(4/3)*np.pi*(r**3)
print("El volumen es: ",end="")
print(v)