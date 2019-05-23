T=int(input())
'''def compositions(n, size):
    if n == 0 and size == 0:
        yield []
    elif 0 < size:
        for i in range(1, n-size+2):
            for c in compositions(n-i, size-1):
                yield c + [i]

'''
def partitions(n, size, limit=None):
    if limit is None:
        limit = n
    if n == 0 and size == 0:
        yield []
    elif size * limit < n:
        pass
    elif 0 < size:
        for i in range(1, min(limit, n-size+1)+1):
            for c in partitions(n-i, size-1, i):
                yield [i] + [c]

while T>0:
    latestarr=[]
    arr=[]
    N,K=map(int , input().split())
    if N==1 or K>=N:
        print(-1)
        continue
    product=1
    for c in partitions(N, K):
        arr.append(c)
    for checker in arr:
        if len(checker) > len(set(checker)):
            arr.remove(checker)
    for check in arr:
        for check1 in check:
            thisone=(check1*check1)-check1
            product=product*thisone
        latestarr.append(product)
        product=1
    m = 1000000007
    print (max(latestarr)%m)
    T-=1
