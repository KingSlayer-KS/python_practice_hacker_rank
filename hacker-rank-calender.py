import calendar
f = list(map(int,input().split()))
u= calendar.weekday(f[2], f[0], f[1])
print(calendar.day_name[u])