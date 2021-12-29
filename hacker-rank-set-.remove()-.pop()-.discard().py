w = int(input())
h = set(map(int, input().split()))
y= int(input())
for i in range (y):
    u= list(map(str, input().split()))
    if u[0] == "remove":
        h.remove(int(u[1]))


    if u[0] == "discard":
        h.discard(int(u[1]))


    if u[0] == "pop":
        h.pop()

print(sum(h))