import numpy

def arrays(arr):
    f= numpy.array(arr,float)
    return f[::-1]
arr = input().strip().split(' ')
result = arrays(arr)
print(result)