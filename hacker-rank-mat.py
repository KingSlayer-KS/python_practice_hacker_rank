t,k = map(int,input().split(" "))
c = ".|."
for i in range(1,t,2):
    print((c*i).center(k,"-"))
for i in range (t):    
    if i == ((t-1)/2):
        print("WELCOME".center(k,"-"))
for i in reversed(range(1,t,2)):
    print((c*i).center(k,"-"))