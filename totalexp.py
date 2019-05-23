T=int(input())
while T>0:
    quantity,price=map(float,input().split())
    if quantity>=1000:
        sum=quantity*price
        discount=sum-(sum*10/100)
        print(str.format('{0:.6f}', discount))
    else:
        print(str.format('{0:.6f}', quantity*price))

    T=T-1
