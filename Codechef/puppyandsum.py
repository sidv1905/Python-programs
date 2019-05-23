T=int(input())
while T>0:
    D,N=map(int , input().split())
    for i in range(D):
        N=int(N*(N+1)//2)
    print(N)
