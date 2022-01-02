from collections import OrderedDict 
f= int(input())
u= OrderedDict()
g= list()
for i in range (f):
    c=list(input().split())
    k=int(c.pop())
    z=" ".join(c)
    if z in u:    
        u[z] = u[z]+int(k)
    else:
        u[z]=int(k)
for z,k in u.items():

    print(z,k)
   



    