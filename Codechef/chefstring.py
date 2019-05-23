T=int(input())
while T>0:
    S1=input()
    S2=input()
    mindiff=0
    maxdiff=0
    for i in range(len(S1)):
        if (S1[i]=='?' or S2[i]=='?' or S1[i]!=S2[i]):
            maxdiff+=1
        if (S1[i]!='?' and S2[i]!='?' and S1[i]!=S2[i]):
            mindiff+=1
    print(mindiff,maxdiff)
    T-=1
