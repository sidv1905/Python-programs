T=int(input())
while T>0:
    A,B,C=map(int,input().split())
    if A+B+C==180:
        print('YES')
    else:
        print('NO')
    T=T-1        
