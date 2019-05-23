t=int(input())

while(t>0):
    N=int(input())
    sum=0
    while(N>0):
        digit=N%10
        sum=sum+digit
        N=N//10
    print(sum)
    t=t-1
