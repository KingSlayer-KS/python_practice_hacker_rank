from itertools import permutations 
f = list((input().split()))
u = list(permutations(f[0],int(f[1])))
u.sort()
for i in u: 
    print("".join(i))