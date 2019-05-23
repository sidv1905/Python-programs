N=input()
if len(N)==10:
    N=int(N)
    sum1=0
    for i in range(10,0,-1):
        digit=N%10
        N=N//10
        sum1=sum1+(digit*i)
    if sum1%11==0:
        print('Legal ISBN')
    else:
        print('Illegal ISBN')
else:
    print('Illegal ISBN')
