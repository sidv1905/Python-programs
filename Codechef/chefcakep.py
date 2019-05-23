T=int(input())
while T>0:
    A,B=map(int, input().split())
    print(max(A,B),A+B)
    T=T-1    
