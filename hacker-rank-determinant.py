import numpy
f=(int(input()))
c=numpy.array([list((input().split())) for i in range(f)],float)
print( numpy.linalg.det(c).round(2))

