T=int(input())
while T>0:
    B=int(input())
    ans=0
    while B>=2:
        B=B-2
        base=B//2
        ans=ans+base
    print(int(ans))
    T=T-1
