#pedimos coordenadas
println("Ingresa la cooredenada r")
r = parse(Float64,readline())
println("Ingresa la cooredenada theta")
theta = parse(Float64,readline())
println("Ingresa la cooredenada phi")
phi = parse(Float64,readline())
#cambio a radianes
theta = theta*pi/180
phi = phi*pi/180
#calculamos el cambio de coordenadas
x = r*sin(phi)*cos(theta)
y = r*sin(phi)*sin(theta)
z= r*cos(phi)
#imprimimos los resultados
println("Las coordenadas cartesianas son:\n(x,y,z) =", (x,y,z))
