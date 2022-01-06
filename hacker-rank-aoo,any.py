f,u =int(input()), list(map(str,input().split()))
k=[(all(int(i)>0 for i in u) and all(int(i)!=0 for i in u)),((any((i[0:]==i[-1::-1] for i in (u)))))]
print(all(k))





 