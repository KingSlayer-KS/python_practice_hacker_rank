from itertools import product 
f = list(map(int,input().split()))
u = list(map(int,input().split()))
c = list(product(f,u))
print(' '.join(str(k) for k in c))