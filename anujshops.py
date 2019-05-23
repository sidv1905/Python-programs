T=int(input())
while T>0:
    sum=0
    A=[]
    As=[]
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.insert(0,K)
    A.sort()
    I=A.index(K)
    print(I)
    As=A[I:]+A[:I]
    print(As)
    for check in As:
        for i in range(1,len(As)):
            subtr=abs(i-check)
            sum=sum+subtr
            break
    print(sum)
    T=T-1
