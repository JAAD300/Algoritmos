println("Calcularemos el volumen de una esfera")
println("Cuál es el radio r de la esfera?")
r=parse(Float64,readline())
println("la clase de r es: ",typeof(r))
v=(4/3)*pi*(r^3)
print("El volumen de la esfera es: ")
println(v)