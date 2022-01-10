import re
c= input()
k= input()
f= re.compile(k)
u=f.search(c)
if not u:
    print("(-1, -1)")

else:
    while u:
      print("({0}, {1})".format(u.start(),u.end()-1))
      u=f.search(c,u.start()+1)

        



