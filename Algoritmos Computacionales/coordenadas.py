import numpy as np
print("Ingresa la cooredenada r")
r = float(input())
print("Ingresa la cooredenada theta")
theta = float(input())
print("Ingresa la cooredenada phi")
phi = float(input())
theta = theta*np.pi/180 #cambio a radianes
phi = phi*np.pi/180
x = r*np.sin(phi)*np.cos(theta)
y = r*np.sin(phi)*np.sin(theta)
z= r*np.cos(phi)
print("Las coordenadas cartesianas son:\n(x,y,z) =", (x,y,z))
