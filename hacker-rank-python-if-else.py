n = int(input().strip())
if n % 2 != 0:
    W ='Weird'
if n % 2 == 0 and 2 <= n <= 5 :
     W ='Not Weird'
if n % 2 == 0 and 6 <= n <= 20 :
     W ='Weird'  
if n % 2 == 0 and n > 20 :
    W ='Not Weird'      
print (W)