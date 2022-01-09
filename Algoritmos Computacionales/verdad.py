#Calculamos tabla de verdad de (P&Q)v(r&(Sv¬Q))&(¬RvS)
#Pedimos inputs
P = bool(input("Dame el valor de P\n"))
Q = bool(input("Dame el valor de Q\n"))
R = bool(input("Dame el valor de R\n"))
S = bool(input("Dame el valor de S\n"))
#Variables auxiliares
A = P and Q
B = (not R) or S
C = S or (not Q)
#Resultados
resultado = A or ((R and C) and B)
print("El valor de la propocición es:", resultado)