w = int(input())
h = set(map(int, input().split()))
y= int(input())
u= set(map(int, input().split()))
hh=h.symmetric_difference(u)
print(len(hh))

