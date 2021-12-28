f = int(input())
u = set(input().split())


c= int(input())
k = set(input().split())


yu = u.symmetric_difference(k)
af=(map(int,yu))

for i in (sorted(af)):
    print(i)





