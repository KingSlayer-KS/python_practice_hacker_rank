import numpy
u=numpy.array(list((input().split())),int)
c=numpy.array(list((input().split())),int)
print (numpy.inner(u, c))
print (numpy.outer(u, c))

