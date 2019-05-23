T=int(input())
while T>0:
    N,M,K=map(int , input().split())
    if(abs(N-M)>K) :
           print(abs(N-M)-K)
    else:
           print(0)
    T=T-1
