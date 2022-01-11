import re
c= int(input())
f=r'(^[7/8/9][0-9]{9})'
for i in range (c):
    u= (input())
    if len(u)== 10:
        k=(bool(re.search((f),u)))
        if k==True:
             print("YES")
        else:
            print("NO")
    else :
        print("NO")
    


        



