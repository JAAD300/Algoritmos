x=[]
f=[]
g=[]
print('{0:^5} {1:^5} {2:^5}'.format('x','f','g')+'\n\n') 
for i in range(0,1001):
    x.append(i*0.1)
    f.append(2*x[i]+1)
    g.append(x[i]**2)  
    print('{0:^5.5} {1:^5.5} {2:^5.5}'.format(x[i],f[i],g[i]))