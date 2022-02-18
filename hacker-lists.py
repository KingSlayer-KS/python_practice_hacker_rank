li = list()
no = int(input())
for i in range (no):
    put = input() .split()
    #print (put)
    if put[0]=='insert':
        li.insert(int(put[1]),int(put[2]))
    if put[0]=='remove':
        li.remove(int(put[1]))
    if put[0]=='append':
        li.append(int(put[1]))
    if put[0]=='print':
        print(li)
    if put[0]=='pop':
        li.pop()
    if put[0]=='reverse':
        li.reverse()
    if put[0]=='sort':
        li.sort()