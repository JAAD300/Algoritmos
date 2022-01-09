c=0
println("ingresa el número máximo")
m=parse(Int64,readline())
while c<=m
    global c
    r=c%3
    if r==0
        println(c," es divisible entre 3")
    end
    c=c+1
end

