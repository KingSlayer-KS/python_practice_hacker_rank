#import numpy as meracodemahan
def average(array):
    a = set(array)
    k = list(a)
    j = sum(a)/len(a)
    #j=meracodemahan.mean(k)
    return j
    

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)