import email.utils 
import re
r= r"^[a-zA-Z][\w.-]+@[a-z]+\.[a-z]{1,3}$"
for i in range (int(input())):
    c=input()
    k=((email.utils.parseaddr(c)))
    u=bool(re.search(re.compile(r),k[1]))
    #print(u) 
    if u == True:
        print(c)
    else:
        continue
