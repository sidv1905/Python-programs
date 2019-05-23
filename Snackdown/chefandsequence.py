T=int(input())
def sumofsquares(A):
    sum1=0
    for i in A:
        sum1+=i*i
    return sum1
while T>0:
    N,K=map(int, input().split())
    arr=list(map(int , input().split()))

    if sumofsquares(arr)<=sum(arr):
        print('YES')
    else:
        for k1 in range(K):
            maxpos = arr.index(max(arr))
            arr[maxpos]=1
            if sumofsquares(arr)<=sum(arr):
                print('YES')
                break
        if sumofsquares(arr)>sum(arr):
            print('NO')

    T-=1
