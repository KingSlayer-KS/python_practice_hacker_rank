w = int(input())
h = set(map(int, input().split()))
y= int(input())
for i in range (y):
    u= list(map(str, input().split()))
    k= set(map(int, input().split()))
    if u[0] == "symmetric_difference_update":
        h.symmetric_difference_update(k)
        
    if u[0] == "intersection_update":
        h.intersection_update(k)
        
    if u[0] == "difference_update":
        h.difference_update(k)
        
    if u[0] == "update":
        h.update(k)

print(sum(h))