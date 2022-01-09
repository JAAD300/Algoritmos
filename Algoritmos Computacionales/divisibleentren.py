c=0
m=int(input("ingresa el número máximo "))

while c<=m:
    r = c%3
    if r == 0:
        print(c," es divisible entre 3")
    c=c+1