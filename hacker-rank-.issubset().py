f= int(input())
for i in range(f):
    u ,c =int(input()), set(map(int,input().split()))
    b ,k = int(input()), set(map(int,input().split()))
    print(c.issubset(k))
