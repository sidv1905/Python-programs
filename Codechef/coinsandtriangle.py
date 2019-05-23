T=int(input())
while T>0:
    N=int(input())
    count=0
    for i in range(N,0,-1):
        N=N-1
        count+=1
        if N==1:
            break
    print(count)
    T=T-1        
