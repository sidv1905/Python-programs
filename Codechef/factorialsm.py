T=int(input())
while T>0:
    N=int(input())
    if N==0:
        print(1)
    else:
        fact=1
        for i in range (2,N+1):
            fact=fact*i
            print(fact)
    T=T-1
