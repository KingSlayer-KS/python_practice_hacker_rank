import numpy

def arrays(arr):
    return (numpy.reshape(numpy.array(arr,int),(3, 3))) 
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)