import numpy
f,u=map(int,input().split())
c=numpy.array([list(map(int,input().split())) for i in range(f)])
m=numpy.sum(c,axis=0)
print(numpy.prod(m))
