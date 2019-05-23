T=int(input())
N=int(input())

count1=0
count2=0
while T>0:
    for i in range(N):
        temp=input()
        temp=int(temp)
        arr.append(temp)
    print(arr)
    for check in arr:
        if check%2!=0:
            for k in range(1,N):
                if arr[k]%2==0:
                    count1+=1
        elif check%2==0:
            for k in range(1,N):
                if arr[k]%2!=0:
                    count2+=1
    print(count2+count1)
    T=T-1
