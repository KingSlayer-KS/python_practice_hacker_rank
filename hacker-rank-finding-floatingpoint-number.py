import re
for i in range (int(input())):
    regex= re.compile(r'^[-\+]?\d*\.\d+$')
    print(bool(re.match(regex,input())))