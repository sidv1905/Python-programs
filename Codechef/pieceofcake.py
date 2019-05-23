T=int(input())
while T>0:
    S=input()
    S=list(S)
    c=0
    for check in S:
        if S.count(check)==len(S)-S.count(check):
            c=1
    if c==1:
        print('YES')
    else:
        print('NO')
    T-=1                
