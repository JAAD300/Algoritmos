println("Ingresa la coordenada x")
x = parse(Float64,readline())
println("Ingresa la coordenada y")
y = parse(Float64,readline())
println("Ingresa la coordenada z")

z = parse(Float64,readline())
r = sqrt(x^2+y^2+z^2)
r0 = sqrt(x^2+y^2)

if z == 0
    theta = pi/2
elseif z > 0
        theta = atan(r0/z)
else
        theta = pi+ atan(r0/z)
end

if x == 0
    phi = sign(y)*(pi/2)
elseif x > 0 && y >= 0
    phi = atan(y/x)
elseif x > 0 && y < 0
    phi = 2*pi + atan(y/x)
elseif x < 0
    phi = pi + atan(y/x)
end

println("Las coordenadas esféricas son:\n(r,theta,phi) =", (r,theta,phi))