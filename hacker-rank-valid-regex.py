import re
f= int(input())

for i in range (f):
    s = input()
    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)
