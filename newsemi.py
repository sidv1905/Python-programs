T=int(input())
while T>0:
    count=0
    N=int(input())
    arr=[6, 10, 14, 15, 21, 22, 26, 33, 34, 35, 38, 39, 46, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95, 106, 111, 115, 118, 119, 122, 123, 129, 133, 134, 141, 142, 143, 145, 146, 155, 158, 159, 161, 166, 177, 178, 183, 185, 187,194 ]
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
