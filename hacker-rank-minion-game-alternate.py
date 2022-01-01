
def minion_game(S):
    s1=0
    s2=0
    vow='AEIOU'
    for i in range(len(S)):
        if S[i] not in vow:
            s1=s1+(len(S)-i)
        else:
            s2=s2+(len(S)-i)   
    if s1>s2:
        print("Stuart",s1)
    elif s2>s1:
        print("Kevin",s2)
    else:
        print("Draw")    


if __name__ == '__main__':
    S = input()
    minion_game(S)





