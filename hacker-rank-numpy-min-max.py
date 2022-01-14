import numpy
f,u=map(int,input().split())
c=numpy.array([list(map(int,input().split())) for i in range(f)])
m=numpy.min(c,axis=1)
print(numpy.max(m,axis=0))
