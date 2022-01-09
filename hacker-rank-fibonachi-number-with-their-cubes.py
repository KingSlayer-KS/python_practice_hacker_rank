from math import sqrt 
cube = lambda x: pow(x,3) 
x=[]

def fibonacci(n):
    if n >0 and n != 0:
        for i in range (n):
            y=int((((1+sqrt(5))**i)-((1-sqrt(5)))**i)/(2**i*sqrt(5)))
            x.append(y)
        return x
    else :
     return x
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))