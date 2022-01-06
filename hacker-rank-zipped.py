g =list(map(int,input().split()))
f=[]
try:
    for i in range (int(g[0])):
        f.append(list(map(float,input().split())))
except EOFError:
    pass
ff=zip(*f)
for i in ff:
    print(sum(i)/(len(i)))


