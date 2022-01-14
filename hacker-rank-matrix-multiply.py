import numpy
f=int(input())
c=numpy.array([list(map(int,input().split())) for i in range(f)])
cx=numpy.array([list(map(int,input().split())) for i in range(f)])
print(numpy.matmul(c,cx))
