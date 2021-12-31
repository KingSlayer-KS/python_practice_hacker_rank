from collections import Counter
no = int(input())
shoes = list(map(int,input().split()))
shoe=Counter(shoes)
n = int(input())
total_bill = 0
for i in range (n):
    cust= list(map(int,input().split()))
    if shoe[cust[0]] != 0 :
        total_bill += cust[1]
        shoe[cust[0]] = shoe[cust[0]]-1

print(total_bill)


