import numpy
def arrays(k,kk):
    f= numpy.array(k,int)
    u= numpy.array(kk,int)
    return(numpy.concatenate((f,u),axis=0)) 
k,kk=[],[]
l= list(map(int,input().split()))
for i in range (l[0]):
    k.append(input().strip().split(' '))
for i in range (l[1]):
    kk.append(input().strip().split(' '))
result= arrays(k,kk)
print(result)

