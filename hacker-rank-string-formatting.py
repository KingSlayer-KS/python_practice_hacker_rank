def print_formatted(num):
    k =bin(num).lstrip("0b")
    for i in range (1,num+1):
        x = i
        v = oct(i).lstrip("0o")
        y= hex(i).lstrip("0x")
        yy = y.upper()
        z =bin(i).lstrip("0b")
        w = len(k)
        o=print(str(x).rjust(w), v.rjust(w), yy.rjust(w), z.rjust(w))
        #print(o)
    return o
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)