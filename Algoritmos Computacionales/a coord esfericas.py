import numpy as np
x = float(input("Ingresa la cooredenada x\n"))
y = float(input("Ingresa la cooredenada y\n"))
z = float(input("Ingresa la cooredenada z\n"))
r = np.sqrt(x**2+y**2+z**2)
r0=np.sqrt(x**2+y**2)
if z==0:
    theta=np.pi/2
elif z>0:
        theta = np.arctan(r0/z)
else:
        theta = np.pi+np.arctan(r0/z)
if x == 0:
    phi = np.sign(y)*(np.pi/2)
elif x > 0 and y >= 0:
    phi = np.arctan(y/x)
elif x > 0 and y < 0:
    phi = 2*np.pi + np.arctan(y/x)
elif x < 0:
    phi = np.pi + np.arctan(y/x)
print("Las coordenadas esféricas son:\n(r,theta,phi) =", (r,theta,phi))