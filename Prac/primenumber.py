T=int(input())
while T>0:
    number = int(input())
    count=0
    if number>1:
        for i in range(2,number):
            if (number % i)==0:
                count+=1
                break
    if count==0:
        print('yes')
    else:
        print('no')
    T=T-1
