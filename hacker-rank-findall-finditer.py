regex_pattern = r"[aeiouAEIOU]{2,}"  # Do not delete 'r'.

import re
for i in (re.findall(regex_pattern, input())):
    if i and len(str(i))>=2:
        print(i)
    else :
        print("-1")

     
       
 