T=int(input())
while T>0:
    arr=[]
    N=int(input())
    for i in range(N):
        S=input()
        if len(S)<=20:
            arr.append(S)
    count=2
    print(arr)
    countarray=[]
    for check in arr:
        check=list(check)
        print(check)
        for i in range(1,len(check)):
            if check[i]=='f' or check[i]=='d':
                if check[i-1]=='j' or check[i-1]=='k':
                    count+=2
                if check[i]=='j' or check[i]=='k':
                    if check[i-1]=='f' or check[i-1]=='d':
                        count+=2
            else:
                count+=4
            print(check[i],check[i-1])
            print(count)
        print(count)
        countarray.append(count)
        count=2
    '''for l in range(len(arr)):
        for l1 in range(l+1,len(arr)):
            if countarray[l]==countarray[l1]:
                    countarray[l1]=countarray[l]//2'''
    print(countarray)
    print(sum(countarray))
    T-=1
