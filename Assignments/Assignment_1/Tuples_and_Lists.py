x=[(2,5),(1,2),(4,4),(2,3),(2,1)]

for i in range(len(x)):
    for j in range(i+1,len(x)):
        y=x[i][-1]  #last element of first tuple
        z=x[j][-1]  #last element of second tuple
        if z<y:
            temp=x[i]
            x[i]=x[j]
            x[j]=temp

print(x)
