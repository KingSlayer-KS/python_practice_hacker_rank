from collections  import namedtuple
n,sum,index = int(input()),0,namedtuple("data",input().split())
for i in range(n):
    sum += int(index(*input().split()).MARKS) 
print(sum/n)
