T=int(input())
while T>0:
    arr=[]
    N=int(input())
    arr=list(map(int , input().split()))
    k=arr[0]
    j=0
    Tsum=0
    countdays=0
    countdaysb=0
    p=0
    while j<=N:
        if arr[j]<len(arr)-1:
            for i in range(0,k+1):
                Tsum=Tsum+arr[i]
                Tsum=int(Tsum)
                p=p+k
            if Tsum < len(arr)-k:
                left=len(arr)-k
                Tsum=Tsum+left
                p=p+left
                if len(arr)==p:
                    countdays+=1
                    break
                else:
                    countdays+=1
            elif Tsum>=len(arr)-k:
                countdaysb+=1
                break
        if arr[j]>=len(arr)-1:
            countdaysb+=1
            break
        j=j+k
    ans=[]
    print(countdays)
    print(countdaysb)
    ans.append(countdaysb)
    ans.append(countdays)
    print(max(ans))
    T-=1
