import numpy
numpy.set_printoptions(legacy='1.13')
l=list(input().split())
f=numpy.array(l,float)
print (numpy.floor(f))
print (numpy.ceil(f))
print (numpy.rint(f))


