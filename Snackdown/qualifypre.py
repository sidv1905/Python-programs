T=int(input())
while T>0:
    count=0
    N,K=map(int, input().split())
    arr=list(map(int , input().split()))
    arr.sort(reverse=True)
    qualified=arr[K-1]
    for check in arr:
        if check>=qualified:
            count+=1
    print(count)
    T-=1
