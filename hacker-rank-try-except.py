f=int(input())
for i in range(f):
    u=list(input().split())
    try:
        print(int(u[0])//int(u[1]))
        
    except ZeroDivisionError as c:
        print ("Error Code:",c)
    
    except ValueError as k:
        print ("Error Code:",k)
