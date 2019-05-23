import itertools
T=int(input())
while T>0:
    N=int(input())
    count=0
    count1=0
    count3=0
    sublist1=(())
    arr=tuple(map(int,input().split()))
    for r in range(N+1):
        sublist=tuple(itertools.combinations(arr,r))
        sublist1+=sublist
    print(sublist1)
    for check in sublist:
        count=check.count(0)
        print(count)
        count1=check.count(1)
        print(count1)
        if count1==count:
            count3+=1
    print(count3)
    T=T-1
