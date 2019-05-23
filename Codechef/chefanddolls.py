T=int(input())
while T>0:
    arr=[]
    c=0
    n=int(input())
    for i in range(n):
        temp=int(input())
        arr.append(temp)
    for check in arr:
        if arr.count(check)%2!=0:
            ans=check
    print(ans)
    T-=1
