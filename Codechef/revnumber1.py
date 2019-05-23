T=int(input())
while T>0:
    N=int(input())
    rev=0
    while N>0:
         digit=N%10
         rev=rev*10+digit
         N=N//10
    print(rev)
    T=T-1     
