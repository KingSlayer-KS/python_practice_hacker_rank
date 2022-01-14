import numpy
n,l=map(int,input().split()  )
f= numpy.array([input().split()for i in range(n)],dtype=int)
b = numpy.array([input().split()for i in range(n)],dtype=int)
print (f+ b)       
print (f- b)
print (f* b)
print (f // b)      
print (f% b)
print (f** b)     

   