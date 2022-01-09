import numpy as np
print("\nCalcularemos la parte real e imaginaria del armónico dado en la tarea\n")
theta = float(input("Ingresa el valor de theta\n"))
phi = float(input("Ingresa el valor de phi\n"))
a = (1/8)*np.sqrt(1155/(2*np.pi))*(np.sin(theta))**2
b = 3*(np.cos(theta))**3-np.cos(theta)
Re = a*b*np.cos(phi)
Im = a*b*np.sin(phi)
print("la parte real es: ",Re)
print("la parte imaginaria es: ",Im)
