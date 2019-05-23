T=int(input())
while T>0:
    arr=[]
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[0]+arr[1])
    T=T-1
