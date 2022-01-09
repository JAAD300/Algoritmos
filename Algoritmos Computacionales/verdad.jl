#Calculamos tabla de verdad de (P&Q)v(r&(Sv¬Q))&(¬RvS)
#Pedimos inputs
println("Dame el valor de P")
P = parse(Bool,readline())
println("Dame el valor de Q")
Q = parse(Bool,readline())
println("Dame el valor de R")
R = parse(Bool,readline())
println("Dame el valor de S")
S = parse(Bool,readline())
#Variables auxiliares
A = P && Q
B = (!R) || S
C = S || (!Q)
#Resultados
resultado = A || ((R && C) && B)
println("El valor de la propocición es: ",resultado)