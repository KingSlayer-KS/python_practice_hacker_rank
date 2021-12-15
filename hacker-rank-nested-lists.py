n =int(input())
mark=list()
lis =list()
Z=list()
for _ in range(n):
    name = input()
    score = float(input())
    lis.append([name,score])
    mark.append(score)
    O = sorted(set(mark))
    m=O
for i in range (n) :
    if m[1] == lis [i-1][1]:
        Z.append(lis[i-1][0])
        Z.sort()
for i in (Z):
    print(i)
