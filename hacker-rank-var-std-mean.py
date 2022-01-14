import numpy
f,u=map(int,input().split())
c=numpy.array([list(map(int,input().split())) for i in range(f)])
print(numpy.mean(c,axis=1))
print(numpy.var(c,axis=0))
k=numpy.std(c,None)
print(k.round(11))