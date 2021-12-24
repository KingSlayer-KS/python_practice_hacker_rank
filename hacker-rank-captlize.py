#!/bin/python3

import os


def solve(s):
    f=list()
    x=s.split(" ")
    for i in x:
       cc= i.capitalize()
       f.append(cc)
    xx=" ".join(f)
    print(xx) 
    return xx
os.environ['OUTPUT_PATH'] = 'o.txt'
fptr = open(os.environ['OUTPUT_PATH'], 'w')

s = input()

result = solve(s)

fptr.write(result + '\n')

fptr.close()
