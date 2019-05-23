T=int(input())
while T>0:
    P1,P2,K=map(int , input().split())
    i=0
    countc=0
    while i<=P1+P2:
        i+=K
        countc+=1
    if countc%2==0:
        print('COOK')
    else:
        print('CHEF')
    T=T-1
