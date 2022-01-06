from collections import defaultdict
f =list(map(int,input().split()))
u,c= int(f[0]),int(f[1])
k=defaultdict(list)
for i in range(1,u+1):
    k[input()].append(i)
m=list()
for i in range(c):
    m.append(input())

for i in m:
    d=k.get(i)
    if d == None:
        print("-1")
    else :
        print(*d)
    
    
