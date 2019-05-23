T=int(input())
while T>0:
    N=int(input())
    restarray=[]
    arr=list(map(int , input().split()))
    checkarray=sorted(arr)
    print(checkarray)
    maximum=max(arr)
    print(maximum)
    indextill=arr.index(maximum)+1
    print(indextill)
    for k in range(indextill,len(arr)):
        restarray.append(arr[k])
    print(restarray)
    for i in range(indextill+1):
        arr[i-indextill]=arr[i]

    print(arr)
    if arr==checkarray:
        print('YES')
    else:
        print('NO')
    T-=1
