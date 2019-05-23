T=int(input())
def subset_sum(numbers, target, partial=[], partial_sum=0):
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n], partial_sum + n)
while T>0:
    arr=[]
    newsubarray=[]
    latestarr=[]

    N,K=map(int , input().split())
    if N==1 or K>N:
        print(-1)
    for i in range(1,N):
        arr.append(i)
    arr=list(subset_sum(arr,N))
    seen = set()
    arr = [item for item in arr if not(tuple(item) in seen or seen.add(tuple(item)))]
    for k in arr:
        if len(k)==K:
            newsubarray.append(k)
    product=1
    for check in newsubarray:
        for check1 in check:
            thisone=(check1*check1)-check1
            product=product*thisone
        latestarr.append(product)
        product=1
    m = 1000000007
    print(max(latestarr)%m)
    T-=1
