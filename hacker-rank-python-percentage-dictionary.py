z =0.00
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
desire_name = input()
a=(student_marks.get(desire_name))
for x in range (0,3):
    z =  z + float(a[x])
print(format(z/3,'.2f'))
#or the simpler way 
#print(format(sum(a)/3,'.2f'))
