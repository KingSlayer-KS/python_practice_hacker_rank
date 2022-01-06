from itertools import combinations_with_replacement
s = list(input().split())   
x=list(combinations_with_replacement(sorted(s[0]),int(s[1])))  
for c in x: 
    print("".join(c))