T=int(input())
while T>0:
    S1,S2=input().split()
    S1=S1.lower()
    S2=S2.lower()
    if sorted(S1)==sorted(S2) and len(S1)==len(S2):
        print('YES')
    else:
        print('NO')
    T=T-1
