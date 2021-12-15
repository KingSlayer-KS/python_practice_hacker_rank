x = int(input())
y = int(input())
z = int(input())
n = int(input())
li= list()
for s in range (x+1):
        for i in range (y+1):
            for z in range (z+1):
                if s+i+z != n:
                    li.append([s, i, z])
print(li)