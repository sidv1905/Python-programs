import math
def checkSemiprime(num):
    cnt = 0

    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            num /= i
            cnt += 1
        if cnt >= 2:
            break
    if(num > 1):
        cnt += 1
    return cnt == 2
T=int(input())
while T>0:
    count=0
    N=int(input())
    arr=[]
    for i in range(N):
        if checkSemiprime(i)==True:
            arr.append(i)
    def is_perfect_square(n):
        return round(n ** 0.5) ** 2 == n
    for check in arr:
        if is_perfect_square(check):
            if check!=25:
                arr.remove(check)
    print(arr)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==N:
                count=1
                break
        if count==1:
            break
    if count==1:
        print('YES')
    else:
        print('NO')
    T-=1
