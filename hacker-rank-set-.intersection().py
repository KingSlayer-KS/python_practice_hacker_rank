w = int(input())
h = set(map(int, input().split()))
y= int(input())
u= set(map(int, input().split()))
hh=h.intersection(u)
print(len(hh))

