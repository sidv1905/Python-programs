while True:
    n=int(input())
    if n == 0:
        break
    arr=list(map(int,input().split()))
    l=[0]*n
    for i in range(1,n+1):
        l[arr[i-1]-1] = i
    if l == arr:
        print('ambiguous')
    else:
        print('not ambiguous')
