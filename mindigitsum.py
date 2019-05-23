T=int(input())
while T>0:
    arr=[]
    N,D=map(int , input().split())
    countd=len(str(N))
    N=int(N)
    while True:
        if countd==1:
            N=N+D
            arr.append(N)
        elif countd==2:
            while N:
                N += N % 10
                N /= 10
            arr.append(N)
            if len(str(N))==1:
                N=N+D
                arr.append(N)
            else:
                break
    print(min(arr))
    T=T-1
