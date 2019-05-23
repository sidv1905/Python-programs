from math import floor
N,Q=map(int,input().split())
arr=list(map(int , input().split()))
while Q>0:
    L,R=map(long , input().split())
    mean=floor((L+R)//2)
    print(long(mean))
    Q=Q-1
