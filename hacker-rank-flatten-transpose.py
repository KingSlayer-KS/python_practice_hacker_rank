import numpy

def arrays(k):
    f= numpy.array(k,int)
    c = f.flatten()
    return("{0}\n{1}".format(numpy.transpose(f),c)) 
    

k=[]
l= list(map(int,input().split()))
for i in range (l[0]):
    k.append(input().strip().split(' '))
result= arrays(k)
print(result)

