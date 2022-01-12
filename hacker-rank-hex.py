import re
in_css = False
for _ in range(int(input())):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for i in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(i)
