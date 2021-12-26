
def minion_game(string):
    Stuart = 0
    Kevin = 0
    
    dd = list(string)
    #print(len(d))
    for c in range (1,len(string)+1):
         for i in range (0,len(s)-c):
             h= string[i:i+(c+1)]
             dd.append(h)
             
    len(dd)
    for i in dd:
        first = str(i[0])
        print(first)
        if first in ("A, E, I, O, U"):
            Kevin  +=1
        #print("yes")
        else : 
            Stuart +=1
    print(Stuart,Kevin)
    if int(Kevin) > int(Stuart):
        print("Kevin", Kevin)
    if int(Kevin) == int(Stuart):
        print("Draw")
    if int(Kevin) < int(Stuart):
        print("Stuart", Stuart)
    


if __name__ == '__main__':
    s = input()
    minion_game(s)





