T=int(input())
while T>0:
    N=int(input())
    first=N//(10**(len(str(N))-1))
    first=int(first)
    N=int(N)
    last=N%10
    last=int(last)
    print(last+first)
    T=T-1
    
