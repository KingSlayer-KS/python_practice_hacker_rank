from collections import deque
f = deque()
u =int(input())
for i in range (u):
    c = list(input().split())
    if c[0]== 'append':
        f.append(int(c[1]))
    if c[0] == 'pop':
        f.pop()
    if c[0] == 'popleft':
        f.popleft()
    if c[0]== 'appendleft' :
        f.appendleft(int(c[1]))
print(f)