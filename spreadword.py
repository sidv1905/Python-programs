T=int(input())
while T>0:
    N=int(input())
    a=list(map( int , input().split()))
    k=a[0]
    tsum=0
    j=0
    while True:
        if k<len(a)-1:
            for i in range(k):
                tsum=tsum+a[i]
                count=1
            if tsum>=len(a)-k:
                count+=1
                break
            elif tsum<len(a)-k:
                count+=1
                continue
            print(count)    
        elif k>=len(a)-1:
            count=1
            break
        k=k+1
        print(k)
    print(count)
    T-=1
