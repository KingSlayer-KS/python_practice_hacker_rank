counter= int(input())
rooms=list(map(str,input().split()))
f,u=set(),set() 
for i in rooms:
    if i not in f:
        f.add(i)
        u.add(i)
    else :