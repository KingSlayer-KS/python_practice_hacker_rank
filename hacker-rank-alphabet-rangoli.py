def print_rangoli(size):
    
    tes =list(map(chr,range(97,123)))
    x =tes[n-1::-1]+tes[1:n]
    l=len("-".join(x))
    for i in range (1,n):
        h= ("-".join(tes[n-1:n-i:-1]+tes[n-i:n])).center(l,"-")
        print(h)
    print("-".join(x))
    for i in reversed(range (1,n)):
        hh= ("-".join(tes[n-1:n-i:-1]+tes[n-i:n])).center(l,"-")

        print(hh)
n = int(input())
print_rangoli(n)    

