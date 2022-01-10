import re
c =input()
f=r'([a-z A-Z 0-9])\1'
u = re.search(f,c)
if u:
    print(u.groups()[0])
else :
    print(-1)