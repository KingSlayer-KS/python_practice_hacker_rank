from itertools import combinations
s = list(input().split())
for i in range (1,int(s[1])+1):   
    x=list(combinations(sorted(s[0]),i))    
    for c in x: 
        print("".join(c))